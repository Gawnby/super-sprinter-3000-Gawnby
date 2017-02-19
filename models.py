from peewee import *
from connect_database import ConnectDatabase


class BaseModel(Model):

    class Meta:
        database = ConnectDatabase.db


class UserStory(BaseModel):
    story_title = CharField()
    user_story = CharField()
    acceptance_criteria = CharField()
    business_value = IntegerField()
    estimation = FloatField()
    status = CharField()

