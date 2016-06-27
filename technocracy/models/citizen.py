from ..webapp import database as db
from uuid import uuid4
from sqlalchemy import Boolean, Column, ForeignKey, Unicode, UnicodeText
from sqlalchemy.orm import backref, relationship, validates
from sqlalchemy_jsonapi import Permissions, permission_test
from sqlalchemy_utils import EmailType, PasswordType, Timestamp, UUIDType

PASSWORD_ENCRYPTION_SCHEMES = ['bcrypt']


class Citizen(Timestamp, db.Model):
    """
    The basic model for a citizen in your government.

    TODO(rico): Create a proper user mixin.
    """

    __tablename__ = 'citizens'

    id = Column(UUIDType, default=uuid4, primary_key=True)
    username = Column(Unicode(30), unique=True, nullable=False)
    email = Column(EmailType, nullable=False)
    password = Column(PasswordType(schemes=PASSWORD_ENCRYPTION_SCHEMES),
                      nullable=False,
                      info={'allow_serialize': False})

    @validates('email')
    def validate_email(self, key, email):
        """Strong email validation."""
        assert '@' in email, 'Not a valid email address.'
        return email

    @validates('username')
    def validate_username(self, key, username):
        """Check the length of the username."""
        assert len(username) >= 4 and len(
            username) <= 30, 'Must be 4 to 30 characters long.'
        return username

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
