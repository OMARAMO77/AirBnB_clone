#!/usr/bin/env python3
"""---"""
import unittest
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """---"""

    def setUp(self):
        """---"""
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.base_model = BaseModel()
        self.user_model = User()
        self.state_model = State()
        self.city_model = City()
        self.amenity_model = Amenity()
        self.place_model = Place()
        self.review_model = Review()

        self.base_model.id = "test_base_id"
        self.user_model.id = "test_user_id"
        self.state_model.id = "test_state_id"
        self.city_model.id = "test_city_id"
        self.amenity_model.id = "test_amenity_id"
        self.place_model.id = "test_place_id"
        self.review_model.id = "test_review_id"

        self.models = [self.base_model, self.user_model, self.state_model,
                       self.city_model, self.amenity_model,
                       self.place_model, self.review_model]

        self.storage._FileStorage__objects = {
            "BaseModel.test_base_id": self.base_model,
            "User.test_user_id": self.user_model,
            "State.test_state_id": self.state_model,
            "City.test_city_id": self.city_model,
            "Amenity.test_amenity_id": self.amenity_model,
            "Place.test_place_id": self.place_model,
            "Review.test_review_id": self.review_model
        }

    def tearDown(self):
        """---"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """---"""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        for model in self.models:
            key = f"{model.__class__.__name__}.{model.id}"
            self.assertIn(key, objects)
            self.assertEqual(objects[key], model)

    def test_new(self):
        """---"""
        new_model = BaseModel()
        self.storage.new(new_model)
        objects = self.storage.all()
        key = f"{new_model.__class__.__name__}.{new_model.id}"
        self.assertIn(key, objects)
        self.assertEqual(objects[key], new_model)

    def test_save_reload(self):
        """---"""
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        objects = self.storage.all()
        for model in self.models:
            key = f"{model.__class__.__name__}.{model.id}"
            self.assertIn(key, objects)
            self.assertIsInstance(objects[key], model.__class__)
            self.assertEqual(objects[key].to_dict(), model.to_dict())


if __name__ == '__main__':
    unittest.main()
