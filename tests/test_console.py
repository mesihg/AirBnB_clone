#!/usr/bin/python3
"""Test for console module"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class Test_Console(unittest.TestCase):
    """Testing console class"""

    def setUp(self):
        """Test setup environment"""
        self.con = HBNBCommand()

    def tearDown(self):
        """Test cleanup"""
        del self.con

    def test_docstrings_in_console(self):
        """Testing for Console docstring"""
        self.assertIsNotNone(self.con.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)

    def test_console_quit(self):
        """Testing quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.con.onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_console_create(self):
        """Testing create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.con.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.con.onecmd("create asdfsfsd")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.con.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            self.con.onecmd("all User")
            self.assertNotEqual("[[User]", f.getvalue()[:7])

    def test_console_show(self):
        """Testing show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.con.onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.con.onecmd("show Test")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.con.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.con.onecmd("show BaseModel abcd-123")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_console_destroy(self):
        """Testing destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.con.onecmd("destroy")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.con.onecmd("destroy Galaxy")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.con.onecmd("destroy User")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.con.onecmd("destroy BaseModel 12345")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

    def test_console_all(self):
        """Testing all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.con.onecmd("all Test")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

    def test_console_update(self):
        """Testing update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.con.onecmd("update")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.con.onecmd("update sldkfjsl")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.con.onecmd("update User")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.con.onecmd("update User 12345")
            self.assertEqual(
                "** attribute name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.con.onecmd("all User")
            obj = f.getvalue()
        my_id = obj[obj.find('(')+1:obj.find(')')]
        with patch('sys.stdout', new=StringIO()) as f:
            self.con.onecmd("update User " + my_id)
            self.assertEqual(
                "** attribute name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.con.onecmd("update User " + my_id + " Name")
            self.assertEqual(
                "** value missing **\n", f.getvalue())


if __name__ == "__main__":
    unittest.main()
