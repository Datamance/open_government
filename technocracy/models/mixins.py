
from inflect import engine
from sqlalchemy import Boolean, Column, Unicode, UnicodeText
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import validates
from sqlalchemy_jsonapi import Permissions, permission_test
from sqlalchemy_utils import EmailType, PasswordType, Timestamp, UUIDType
from uuid import uuid4

PASSWORD_ENCRYPTION_SCHEMES = ['bcrypt']

inflector = engine()


class BaseEntityMixin(Timestamp):
    """The base model for every modeled entity."""

    @declared_attr
    def __tablename__(cls):
        return inflector.plural(cls.__name__.lower())

    id = Column(UUIDType, default=uuid4, primary_key=True)

    def __repr__(self):
        return '<{entity_type}-{id}>'.format(
            entity_type=self.__class__, id=self.id)


class User(BaseEntityMixin):
    """Mixin for users - admins, citizens, etc."""
    name = Column(Unicode(30), unique=True, nullable=False)
    email = Column(EmailType, nullable=False)
    password = Column(PasswordType(schemes=PASSWORD_ENCRYPTION_SCHEMES),
                      nullable=False,
                      info={'allow_serialize': False})

    @validates('email')
    def validate_email(self, key, email):
        """Strong email validation."""
        assert '@' in email, 'Not a valid email address.'
        return email

    @validates('name')
    def validate_name(self, key, name):
        """Check the length of the name."""
        assert len(name) >= 4 and len(
            name) <= 30, 'Must be 4 to 30 characters long.'
        return name

    @validates('password')
    def validate_password(self, key, password):
        """Validate a password's length."""
        assert len(password) >= 5, 'Password must be 5 characters or longer.'
        return password

    @permission_test(Permissions.VIEW, 'password')
    def view_password(self):
        """Never let the password be seen."""
        return False

    @permission_test(Permissions.DELETE)
    def allow_delete(self):
        """You should be able to get rid of your presence."""
        return True


class Document(BaseEntityMixin):
    """Anything with text and meta.

    Note: At the time, I'm not enforcing any authorship norms. Those
    are to be defined on their respective ORM classes.
    """
    title = Column(Unicode(100), nullable=False)
    content = Column(UnicodeText, nullable=False)
    published = Column(Boolean, default=False)

    @validates('title')
    def validate_title(self, key, title):
        """Keep titles from getting too long."""
        assert len(title) >= 5 or len(
            title) <= 100, 'Must be 5 to 100 characters long.'
        return title
