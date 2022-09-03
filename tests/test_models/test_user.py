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
        return super().setUp()

    def tearDown(self):
        """Test cleanup"""
        del(self.user)
        return super().tearDown()

    def test_user_instance(self):
        """Test if instanceof User"""
        self.assertIsInstance(self.user, User)

    def test_basemodel_instance(self):
        """Test if instanceof BaseModel"""
        self.assertIsInstance(self.user, BaseModel)


if __name__ == '__main__':
    unittest.main()
