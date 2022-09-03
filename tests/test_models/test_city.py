#!/usr/bin/python3

"""Test for city module"""

import unittest
from models.city import City
from models.base_model import BaseModel


class Test_User(unittest.TestCase):
    """"Testing City class"""
    def setUp(self):
        """Test setup environment"""
        self.city = City()
        return super().setUp()

    def tearDown(self):
        """Test cleanup"""
        del(self.city)
        return super().tearDown()

    def test_user_instance(self):
        """Test if instanceof City"""
        self.assertIsInstance(self.city, City)

    def test_basemodel_instance(self):
        """Test if instanceof BaseModel"""
        self.assertIsInstance(self.city, BaseModel)


if __name__ == '__main__':
    unittest.main()
