#!/usr/bin/python3

"""Test for user module"""

import unittest
from models.user import User
from models.base_model import BaseModel


class Test_User(unittest.TestCase):
    """"Testing User class"""
    def setUp(self):
        """Test setup environment"""
        self.user = User()

    def tearDown(self):
        """Test cleanup"""
        del self.user

    def test_user_docstring(self):
        """Testing for user docstring"""
        self.assertIsNotNone(User.__doc__)

    def test_user_attributes(self):
        """Testing user attributes"""
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)

    def test_user_instance(self):
        """Test if instanceof User"""
        self.assertIsInstance(self.user, User)

    def test_basemodel_isinstance(self):
        """Testing if User is an instance of Basemodel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_user_attribute_types(self):
        """Testing user attribute types"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    def test_user_save(self):
        """Testing user save method"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_save_with_arg(self):
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)

    def test_save_updates_file(self):
        user = User()
        user.save()
        userid = "User." + user.id
        with open("file.json", "r") as f:
            self.assertIn(userid, f.read())

    def test_user_to_dict(self):
        """Testing user to_dict method"""
        self.assertEqual('to_dict' in dir(self.user), True)


if __name__ == '__main__':
    unittest.main()
