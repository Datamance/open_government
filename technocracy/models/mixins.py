from uuid import uuid4
from sqlalchemy import Boolean, Column, ForeignKey, Unicode, UnicodeText
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import backref, relationship, validates
from sqlalchemy_jsonapi import Permissions, permission_test
from sqlalchemy_utils import EmailType, PasswordType, Timestamp, UUIDType

PASSWORD_ENCRYPTION_SCHEMES = ['bcrypt']


class BaseEntityMixin(Timestamp):
    """The base model for every modeled entity."""

    @declared_attr
    def __tablename__(cls):
        return '{!s}s'.format(cls.__name__.lower())

    id = Column(UUIDType, default=uuid4, primary_key=True)


class User(BaseEntityMixin):
    """
    Mixin for users - admins, citizens, etc.
    """
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

    def __repr__(self):
        return 'Citizen {}>'.format(self.id)
