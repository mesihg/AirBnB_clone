#!/usr/bin/python3

"""Test for base_model module"""

import unittest
from models.base_model import BaseModel


class Test_User(unittest.TestCase):
    """"Testing BaseModel class"""
    def setUp(self):
        """Test setup environment"""
        self.base = BaseModel()
        self.name = "My First Model"
        self.my_number = 89

    def tearDown(self):
        """Test cleanup"""
        del self.base

    def test_basemodel_docstring(self):
        """Testing for BaseModel docstring"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_basemodel_methods(self):
        """Testing for BaseModel methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_basemodel_instance(self):
        """Test if instanceof BaseModel"""
        self.assertIsInstance(self.base, BaseModel)

    def test_basemodel_save(self):
        """Testing BaseModel save method"""
        self.base.save()
        self.assertEqual(self.base.create_at, self.base.update_at)

    def test_basemodel_to_dict(self):
        """Testing BaseModel to_dict method"""
        dct = self.base.to_dict()
        self.assertIsInstance(dct['created_at'], str)
        self.assertIsInstance(dct['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
