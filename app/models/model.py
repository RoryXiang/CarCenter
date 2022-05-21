import datetime
from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255)
    phone = fields.CharField(max_length=11)
    password = fields.CharField(max_length=50)
    email = fields.CharField(max_length=255)
    creator = fields.IntField(default=0)
    create_time = fields.DatetimeField(auto_now=True)
    update_time = fields.DatetimeField(auto_now_add=True)
    is_deleted = fields.IntField(default=0)
    is_admin = fields.IntField(default=0)


is_deleted = fields.IntField(default=0)


class Meta:
        table = 'users'
