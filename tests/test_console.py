#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.user import User


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.hbnb = HBNBCommand()

    def tearDown(self):
        self.hbnb = None

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd('create BaseModel')
            instance_id = f.getvalue().strip()
            self.hbnb.onecmd(f'show BaseModel {instance_id}')
            output = f.getvalue().strip()
            self.assertTrue("[BaseModel]" in output and instance_id in output)

    def test_create_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("create User")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)

    def test_create_state(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("create State")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)

    def test_create_city(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("create City")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)

    def test_create_amenity(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("create Amenity")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)

    def test_create_place(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("create Place")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)

    def test_create_review(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("create Review")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)

    def test_show_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd('create User')
            instance_id = f.getvalue().strip()
            self.hbnb.onecmd(f'show User {instance_id}')
            output = f.getvalue().strip()
            self.assertTrue("[User]" in output and instance_id in output)

    def test_show_state(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd('create State')
            instance_id = f.getvalue().strip()
            self.hbnb.onecmd(f'show State {instance_id}')
            output = f.getvalue().strip()
            self.assertTrue("[State]" in output and instance_id in output)

    def test_show_city(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd('create City')
            instance_id = f.getvalue().strip()
            self.hbnb.onecmd(f'show City {instance_id}')
            output = f.getvalue().strip()
            self.assertTrue("[City]" in output and instance_id in output)

    def test_show_amenity(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd('create Amenity')
            instance_id = f.getvalue().strip()
            self.hbnb.onecmd(f'show Amenity {instance_id}')
            output = f.getvalue().strip()
            self.assertTrue("[Amenity]" in output and instance_id in output)

    def test_show_place(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd('create Place')
            instance_id = f.getvalue().strip()
            self.hbnb.onecmd(f'show Place {instance_id}')
            output = f.getvalue().strip()
            self.assertTrue("[Place]" in output and instance_id in output)

    def test_show_review(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd('create Review')
            instance_id = f.getvalue().strip()
            self.hbnb.onecmd(f'show Review {instance_id}')
            output = f.getvalue().strip()
            self.assertTrue("[Review]" in output and instance_id in output)

    def test_all_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd('create User')
            self.hbnb.onecmd('create User')
            self.hbnb.onecmd('all User')
            output = f.getvalue().strip()
            self.assertTrue("[User]" in output)

    def test_all_state(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd('create State')
            self.hbnb.onecmd('create State')
            self.hbnb.onecmd('all State')
            output = f.getvalue().strip()
            self.assertTrue("[State]" in output)

    def test_all_city(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd('create City')
            self.hbnb.onecmd('create City')
            self.hbnb.onecmd('all City')
            output = f.getvalue().strip()
            self.assertTrue("[City]" in output)

    def test_all_amenity(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd('create Amenity')
            self.hbnb.onecmd('create Amenity')
            self.hbnb.onecmd('all Amenity')
            output = f.getvalue().strip()
            self.assertTrue("[Amenity]" in output)

    def test_all_place(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd('create Place')
            self.hbnb.onecmd('create Place')
            self.hbnb.onecmd('all Place')
            output = f.getvalue().strip()
            self.assertTrue("[Place]" in output)

    def test_all_review(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd('create Review')
            self.hbnb.onecmd('create Review')
            self.hbnb.onecmd('all Review')
            output = f.getvalue().strip()
            self.assertTrue("[Review]" in output)


if __name__ == '__main__':
    unittest.main()
