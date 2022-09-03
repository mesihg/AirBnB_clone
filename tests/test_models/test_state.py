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
        return super().setUp()

    def tearDown(self):
        """Test cleanup"""
        del(self.state)
        return super().tearDown()

    def test_state_instance(self):
        """Test if instanceof State"""
        self.assertIsInstance(self.state, State)

    def test_basemodel_instance(self):
        """Test if instanceof BaseModel"""
        self.assertIsInstance(self.state, BaseModel)


if __name__ == '__main__':
    unittest.main()
