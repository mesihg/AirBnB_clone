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
        return super().setUp()

    def tearDown(self):
        """Test cleanup"""
        del(self.storage)
        del(self.model)
        if os.path.exists("file.json"):
            os.remove("file.json")
        return super().tearDown()

    def test_isinstance(self):
        """Test for instanceof"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_save(self):
        base = BaseModel()
        models.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        base = BaseModel()
        models.storage.save()
        models.storage.reload()
        for bobjs in models.storage.all().values():
            objs = bobjs
        self.assertEqual(base.to_dict()['id'], objs.to_dict()['id'])


if __name__ == '__main__':
    unittest.main()
