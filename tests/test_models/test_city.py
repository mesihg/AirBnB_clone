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

    def tearDown(self):
        """Test cleanup"""
        del self.city

    def test_city_docstring(self):
        """Testing for City docstring"""
        self.assertIsNotNone(City.__doc__)

    def test_city_attributes(self):
        """Testing City attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)

    def test_city_instance(self):
        """Test if instanceof City"""
        self.assertIsInstance(self.city, City)

    def test_city_state_id(self):
        """Testing city state_id"""
        self.assertEqual(str, type(City.state_id))

    def test_city_name(self):
        """Testing city name"""
        self.assertEqual(type(City.name), str)

    def test_basemodel_instance(self):
        """Test if instanceof BaseModel"""
        self.assertIsInstance(self.city, BaseModel)

    def test_city_save(self):
        """Testing City save method"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_city_to_dict(self):
        """Testing city to_dict method"""
        dct = self.city.to_dict()
        self.assertIsInstance(dct['created_at'], str)
        self.assertIsInstance(dct['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
