#!/usr/bin/python3

"""Test for amenity module"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class Test_User(unittest.TestCase):
    """"Testing Amenity class"""
    def setUp(self):
        """Test setup environment"""
        self.amenity = Amenity()
        return super().setUp()

    def tearDown(self):
        """Test cleanup"""
        del(self.amenity)
        return super().tearDown()

    def test_user_instance(self):
        """Test if instanceof Amenity"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_basemodel_instance(self):
        """Test if instanceof BaseModel"""
        self.assertIsInstance(self.amenity, BaseModel)


if __name__ == '__main__':
    unittest.main()
