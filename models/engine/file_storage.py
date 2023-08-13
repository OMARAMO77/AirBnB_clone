#!/usr/bin/python3
"""---"""
import json
from models.base_model import BaseModel
from models.user import User
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import path


class FileStorage:
    """---"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """---"""
        return self.__objects

    def new(self, obj):
        """---"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """---"""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """---"""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                json_content = f.read()
                json_dict = json.loads(json_content)
                for key, value in json_dict.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
