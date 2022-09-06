#!/usr/bin/python3
"""Test for file storage module"""


import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
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

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)

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
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + cy.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Review." + rv.id, objs)

    def test_new(self):
        """Testing new method"""
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
