#!/usr/bin/python3
""" This will create the base code for the Airbnb clone """
import uuid
from datetime import datetime
import json


class BaseModel:
    """ The base of all other model """

    def __init__(self, id, created_at, updated_at):
        """
        id is generated woth the uuid random unique
        value generatir and it is converted to a string
        created_at is the date of creation.
        updated_at is the date of each modification.
        """
        random_id = uuid.uuid4()
        id = str(random_id)
        self.id = id
        created_at = datetime.now()
        self.created_at = created_at
        self.updated_at = created_at

    def __str__(self):
        """
        this will print out the string of
        [<class name>] (<self.id>) <self.__dict__>
        """
        print(f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')

    def save(self):
        """
        this will update the datetime when an instance is saved
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        This will change the inputted words inti dictionary
        """
        self.__class__ = self.__class__.__name__
        self.created_at = created_at.isoformat()
        self.updated_at = updated_at.isoformat()
        obj_string = f'{ "name":{self.__class__}, "id":{self.id}, \
                "created_at":{self.created_at}, \
                "updated_at":{self.updated_at}}'
        self.__dict__ = json.loads(obj_string)
        return self.__dict__
