#!/usr/bin/python3
"""---"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """---"""

    def test_amenity_attribute(self):
        """---"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))


if __name__ == '__main__':
    unittest.main()
