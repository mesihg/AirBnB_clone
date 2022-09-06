#!/usr/bin/python3

"""Test for amenity module"""

import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class Test_User(unittest.TestCase):
    """"Testing Amenity class"""
    def setUp(self):
        """Test setup environment"""
        self.amenity = Amenity()

    def tearDown(self):
        """Test cleanup"""
        del self.amenity
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_docstring_amenity(self):
        """Testing for Amenity docstring"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_amenity(self):
        """Testing for attributes of Amenity"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertFalse('name' in self.amenity.__dict__)

    def test_amenity_instance(self):
        """Testing if instanceof Amenity"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_amenity_subclass(self):
        """Testing if Amenity is subclass of BaseModel"""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))
    
    def test_amenity_name(self):
        """Testing Amenity name"""
        self.assertTrue(type(self.amenity.name), str)

    def test_amenity_save(self):
        """Testing if amenities are saved"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)


if __name__ == '__main__':
    unittest.main()
