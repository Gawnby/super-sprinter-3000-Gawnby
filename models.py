from peewee import *


class CreateDatabase:
    @staticmethod
    def create_db_object():
        recognize_db = open("connect_str.txt", "r")
        login = recognize_db.readlines()
        recognize_db.close()
        db = PostgresqlDatabase(login[0], user=login[0])
        return db


class BaseModel(Model):
    class Meta:
        database = CreateDatabase.create_db_object()


class Entries(BaseModel):
    story_title = CharField()
    user_story = CharField()
    acceptance_criteria = CharField()
    business_value = IntegerField()
    estimation = FloatField()
    status = CharField()

    