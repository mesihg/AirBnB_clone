#!/usr/bin/python3
"""Test for console module"""
import unittest
from unittest.mock import patch
from io import StringIO
from models import storage
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

    def test_console_show_no_instance_found(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show(1)"))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.show(1)"))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("State.show(1)"))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("City.show(1)"))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show(1)"))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Place.show(1)"))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Review.show(1)"))
            self.assertEqual("** no instance found **", f.getvalue().strip())

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
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy(1)"))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.destroy(1)"))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("State.destroy(1)"))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("City.destroy(1)"))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy(1)"))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy(1)"))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy(1)"))
            self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_console_all(self):
        """Testing all command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertIn("BaseModel", f.getvalue().strip())
            self.assertNotIn("User", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertIn("User", f.getvalue().strip())
            self.assertNotIn("BaseModel", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all State"))
            self.assertIn("State", f.getvalue().strip())
            self.assertNotIn("BaseModel", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all City"))
            self.assertIn("City", f.getvalue().strip())
            self.assertNotIn("BaseModel", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
            self.assertIn("Amenity", f.getvalue().strip())
            self.assertNotIn("BaseModel", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
            self.assertIn("Place", f.getvalue().strip())
            self.assertNotIn("BaseModel", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all Review"))
            self.assertIn("Review", f.getvalue().strip())
            self.assertNotIn("BaseModel", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", f.getvalue().strip())
            self.assertNotIn("User", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertIn("User", f.getvalue().strip())
            self.assertNotIn("BaseModel", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertIn("State", f.getvalue().strip())
            self.assertNotIn("BaseModel", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertIn("City", f.getvalue().strip())
            self.assertNotIn("BaseModel", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertIn("Amenity", f.getvalue().strip())
            self.assertNotIn("BaseModel", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertIn("Place", f.getvalue().strip())
            self.assertNotIn("BaseModel", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertIn("Review", f.getvalue().strip())
            self.assertNotIn("BaseModel", f.getvalue().strip())

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
                "** no instance found **\n", f.getvalue())
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
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            tId = output.getvalue().strip()
        testCmd = "BaseModel.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["BaseModel.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            tId = output.getvalue().strip()
        testCmd = "User.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["User.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            tId = output.getvalue().strip()
        testCmd = "State.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["State.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            tId = output.getvalue().strip()
        testCmd = "City.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["City.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            tId = output.getvalue().strip()
        testCmd = "Place.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            tId = output.getvalue().strip()
        testCmd = "Amenity.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Amenity.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            tId = output.getvalue().strip()
        testCmd = "Review.update({}, attr_name, 'attr_value')".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Review.{}".format(tId)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_console_count(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertNotEqual("1", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertNotEqual("1", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertNotEqual("1", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertNotEqual("1", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertNotEqual("1", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertNotEqual("1", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertNotEqual("1", f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
