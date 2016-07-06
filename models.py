#!usr/bin/python

import datetime

from flask_bcrypt import generate_password_hash
from flask.ext.login import UserMixin
import peewee

DATABASE = peewee.PostgresqlDatabase('social.db', User='postgres')

class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BoolleanField(default=False)

class meta:
    database = DATABASE
    order_by = ('joined_at')

@classmethod
def create_user(cls, username, email, password, admin=False):
    try:
        cls.create(
            username=username,
            password=generate_password_hash(password),
            email=email,
            is_admin=admin
        )
    except IntegrityError:
        raise ValueError('User already exists')

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([user], safe=True)
    DATABASE.close()
