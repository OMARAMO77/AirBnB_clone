#!/usr/bin/python3
"""---"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest


class TestConsole(unittest.TestCase):
    """---"""
    def test_class(self):
        """---"""
        city_1 = City()
        amenity_1 = Amenity()
        state_1 = State()
        review_1 = Review()
        place_1 = Place()
        self.assertEqual(city_1.__class__.__name__, "City")
        self.assertEqual(amenity_1.__class__.__name__, "Amenity")
        self.assertEqual(state_1.__class__.__name__, "State")
        self.assertEqual(review_1.__class__.__name__, "Review")
        self.assertEqual(place_1.__class__.__name__, "Place")

    def test_father(self):
        """---"""
        city_1 = City()
        amenity_1 = Amenity()
        state_1 = State()
        review_1 = Review()
        place_1 = Place()
        self.assertTrue(issubclass(city_1.__class__, BaseModel))
        self.assertTrue(issubclass(amenity_1.__class__, BaseModel))
        self.assertTrue(issubclass(state_1.__class__, BaseModel))
        self.assertTrue(issubclass(review_1.__class__, BaseModel))
        self.assertTrue(issubclass(place_1.__class__, BaseModel))
