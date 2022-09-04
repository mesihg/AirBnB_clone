#!/usr/bin/python3

"""Test for state module"""

import unittest
from models.state import State
from models.base_model import BaseModel


class Test_State(unittest.TestCase):
    """"Testing State class"""
    def setUp(self):
        """Test setup environment"""
        self.state = State()
        self.state.name = "AA"

    def tearDown(self):
        """Test cleanup"""
        del self.state

    def test_state_docstring(self):
        """Testing for state docstring"""
        self.assertIsNotNone(State.__doc__)

    def test_state_attributes(self):
        """Testing State attributes"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_basemodel_isinstance(self):
        """Testing if State is an instance of BaseModel"""
        self.assertIsInstance(self.state, BaseModel)

    def test_state_attribute_types(self):
        """Testing state attribute types"""
        self.assertEqual(type(self.state.name), str)

    def test_state_save(self):
        """Testing state save method"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_state_to_dict(self):
        """Testing state to_dict method"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == '__main__':
    unittest.main()
