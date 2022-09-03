#!/usr/bin/python3

"""Test for base_model module"""

import unittest
from models.base_model import BaseModel


class Test_User(unittest.TestCase):
    """"Testing BaseModel class"""
    def setUp(self):
        """Test setup environment"""
        self.base = BaseModel()
        return super().setUp()

    def tearDown(self):
        """Test cleanup"""
        del(self.base)
        return super().tearDown()

    def test_basemodel_instance(self):
        """Test if instanceof BaseModel"""
        self.assertIsInstance(self.base, BaseModel)


if __name__ == '__main__':
    unittest.main()
