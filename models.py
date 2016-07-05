#!usr/bin/python

import datetime
from peewee import *

DATABASE = PostgresDatabase('social.db')

class User(Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BoolleanField(default=False)

class meta:
    database = DATABASE
    order_by = ('joined_at')

