#!/usr/bin/python3
"""---"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    to test state
    """

    def test_state_attribute(self):
        """
        testing the state attributes
        """
        state = State()
        self.assertTrue(hasattr(state, 'name'))


if __name__ == '__main__':
    unittest.main()
