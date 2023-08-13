#!/usr/bin/python3
"""---"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """---"""

    def test_city_attributes(self):
        """---"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))


if __name__ == '__main__':
    unittest.main()
