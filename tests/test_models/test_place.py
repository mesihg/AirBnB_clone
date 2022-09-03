#!/usr/bin/python3

"""Test for place module"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class Test_Place(unittest.TestCase):
    """"Testing Place class"""
    def setUp(self):
        """Test setup environment"""
        self.place = Place()
        return super().setUp()

    def tearDown(self):
        """Test cleanup"""
        del(self.place)
        return super().tearDown()

    def test_review_instance(self):
        """Test if instanceof Place"""
        self.assertIsInstance(self.place, Place)

    def test_basemodel_instance(self):
        """Test if instanceof BaseModel"""
        self.assertIsInstance(self.place, BaseModel)


if __name__ == '__main__':
    unittest.main()
