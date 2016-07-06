#!usr/bin/python

from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import Email, EqualTo, Length, Regexp, DataRequired, ValidationError

from models import User

def name_exists(form, field):
    if User.select().where(User.username==field.data).exists():
        raise ValidationError('User with that name already exists')

def email_exists():
    if User.select().where(User.email==field.data).exists():
        raise ValidationError('User with that email already exists')


class RegisterForm(Form):
    username = StringField('Username',
                           validators= [
                               DataRequired(),
                               Regexp(r'^[a-zA-Z0-9_]+$',
                               message=("username should be one word, letters"
                                        "numbers and underscores only"), name_exists

                           ])
    email = StringField(
        'Email',
        validators= [
            Email(),
            DataRequired(),
            email_exists
        ]

    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=4),
            EqualTo('password2', message="password must match")

        ]
    )
    password2 = PasswordField(
        'Confirm Password',
        validators = [
            DataRequired()
        ]
    )