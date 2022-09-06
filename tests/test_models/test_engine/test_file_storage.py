#!/usr/bin/python3
"""Test for file storage module"""


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
import os


class Test_file_storage(unittest.TestCase):
    """"Testing file storage engine class"""
    def setUp(self):
        """Test setup environment"""
        self.model = BaseModel()
        self.storage = FileStorage()

    def tearDown(self):
        """Test cleanup"""
        del self.storage
        del self.model
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_storage_isinstance(self):
        """Test for instanceof"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_basemodel_isinstance(self):
        """Testing model if its an instance of BaseModel"""
        self.assertIsInstance(self.model, BaseModel)

    def test_storage_instance(self):
        """Testing models.storage as an instance of FileStorage"""
        self.assertEqual(type(models.storage), FileStorage)

    def test_all(self):
        """Testing all method"""
        objs = models.storage.all()
        self.assertIsNotNone(objs)
        self.assertEqual(dict, type(objs))

    def test_all_with_arg(self):
        """Testing all method with arg"""
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_save(self):
        """Testing save method"""
        base = BaseModel()
        models.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Testing reload method"""
        base = BaseModel()
        models.storage.save()
        models.storage.reload()
        for bobjs in models.storage.all().values():
            objs = bobjs
        self.assertEqual(base.to_dict()['id'], objs.to_dict()['id'])

    def test_new(self):
        basemodel = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(basemodel)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        self.assertIn("BaseModel." + basemodel.id, models.storage.all().keys())
        self.assertIn(basemodel, models.storage.all().values())
        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn(user, models.storage.all().values())
        self.assertIn("State." + state.id, models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())
        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())
        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())
        self.assertIn("Amenity." + amenity.id, models.storage.all().keys())
        self.assertIn(amenity, models.storage.all().values())
        self.assertIn("Review." + review.id, models.storage.all().keys())
        self.assertIn(review, models.storage.all().values())


if __name__ == '__main__':
    unittest.main()
