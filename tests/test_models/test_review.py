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
        self.review.place_id = "6 killo"
        self.review.user_id = "123-AA"
        self.review_text = "The best stuff in town"

    def tearDown(self):
        """Test cleanup"""
        del self.review

    def test_review_docstring(self):
        """Testing for review docstring"""
        self.assertIsNotNone(Review.__doc__)

    def test_review_attributes(self):
        """Testing review attributes"""
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)

    def test_basemodel_isinstance(self):
        """Testing if review is an instance of BaseModel"""
        self.assertIsInstance(self.review, BaseModel)

    def test_review_attribute_types(self):
        """Testing review attribute types"""
        self.assertEqual(type(self.review.text), str)
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)

    def test_review_save(self):
        """Testing review save method"""
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_review_to_dict(self):
        """Testing review to_dict method"""
        self.assertEqual('to_dict' in dir(self.review), True)


if __name__ == '__main__':
    unittest.main()
