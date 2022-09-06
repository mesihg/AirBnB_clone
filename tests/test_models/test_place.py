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

    def tearDown(self):
        """Test cleanup"""
        del self.place

    def test_place_attributes(self):
        """Testing for Place attributes"""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)

    def test_place_no_arg(self):
        """Testing Place for no argument """
        self.assertEqual(Place, type(Place()))

    def test_place_isinstance(self):
        """Testing if place is an instance of Place"""
        self.assertIsInstance(self.place, Place)

    def test_basemodel_isinstance(self):
        """Testing if Place is an instance of Basemodel"""
        self.assertIsInstance(self.place, BaseModel)

    def test_place_attribute_type(self):
        """Testing Place attribute types"""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_place_save(self):
        """Testing Place save method"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_place_to_dict(self):
        """Testing place to_dict method"""
        self.assertEqual('to_dict' in dir(self.place), True)


if __name__ == '__main__':
    unittest.main()
