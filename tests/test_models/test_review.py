#!/usr/bin/python3

"""Test for review module"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class Test_State(unittest.TestCase):
    """"Testing Review class"""
    def setUp(self):
        """Test setup environment"""
        self.review = Review()
        return super().setUp()

    def tearDown(self):
        """Test cleanup"""
        del(self.review)
        return super().tearDown()

    def test_review_instance(self):
        """Test if instanceof State"""
        self.assertIsInstance(self.review, Review)

    def test_basemodel_instance(self):
        """Test if instanceof BaseModel"""
        self.assertIsInstance(self.review, BaseModel)


if __name__ == '__main__':
    unittest.main()
