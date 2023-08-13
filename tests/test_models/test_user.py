"""---"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    testing the user file
    """

    def test_user_attributes(self):
        """ use to test the attribute in user file """
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))


if __name__ == '__main__':
    unittest.main()
