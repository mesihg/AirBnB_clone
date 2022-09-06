#!/usr/bin/python3

"""Test for place module"""

import unittest
import os
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
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_place_attributes(self):
        """Testing for Place attributes"""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)

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

    def test_place_city_id(self):
        """Testing place city_id"""
        self.assertEqual(type(Place.city_id), str)

    def test_place_user_id(self):
        """Testing place user_id"""
        self.assertEqual(type(Place.user_id), str)

    def test_place_name(self):
        """Testing place name"""
        self.assertEqual(type(Place.name), str)

    def test_place_description(self):
        """Testing place description"""
        self.assertEqual(type(Place.description), str)

    def test_place_number_rooms(self):
        """Testing place number of rooms"""
        self.assertEqual(type(Place.number_rooms), int)

    def test_place_number_bathrooms(self):
        """Testing place number of bathrooms"""
        self.assertEqual(type(Place.number_bathrooms), int)

    def test_place_max_guest(self):
        """Testing place max guest"""
        self.assertEqual(type(Place.max_guest), int)

    def test_place_price_by_night(self):
        """Testing place price by ngiht"""
        self.assertEqual(type(Place.price_by_night), int)

    def test_place_latitude(self):
        """Testing place latitude"""
        self.assertEqual(type(Place.latitude), float)

    def test_place_longitude(self):
        """Testing place longitude"""
        self.assertEqual(type(Place.longitude), float)

    def test_place_amenity_ids(self):
        """Testing place amenity ids"""
        self.assertEqual(list, type(Place.amenity_ids), list)

    def test_place_save(self):
        """Testing Place save method"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_place_to_dict(self):
        """Testing place to_dict method"""
        self.assertEqual('to_dict' in dir(self.place), True)


if __name__ == '__main__':
    unittest.main()
