#!/usr/bin/python3
"""command interpreter console module"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


classes = {"BaseModel": BaseModel,
           "User": User,
           "State": State,
           "City": City,
           "Amenity": Amenity,
           "Place": Place,
           "Review": Review
           }


class HBNBCommand(cmd.Cmd):
    """A Class that contains the entry point of the command interpreter"""

    prompt = "(hbnb) "

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if not line:
            print("** class name missing **")
        elif line not in classes:
            print("** class doesn't exist **")
        else:
            cls = classes[line]()
            print(cls.id)
            cls.save()

    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = line.split()
        obj_data = models.storage.all()
        if args[0] not in classes:
            print("** class name missing **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in obj_data:
                print("** no instance found **")
            else:
                print(obj_data[key])
                return

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        obj_data = models.storage.all()
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in classes:
                print("** class doesn't exist **")
            elif len(args) != 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in obj_data:
                    print("** no instance found **")
                else:
                    # del obj_data[key]
                    obj_data.pop(key)
                    models.storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances"""
        obj_data = models.storage.all()
        args = line.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in obj_data.values():
                if args[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(args) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id:"""
        if not line:
            print("** class name missing **")
            return
        else:
            args = line.split()
            obj_data = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            if args[0] not in classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            elif key not in obj_data:
                print("** no instance found **")
            else:
                attr = args[2]
                value = args[3].replace('"', ' ')
                inst = obj_data[key]

                if hasattr(inst, attr) and type(getattr(inst, attr)) is int:
                    if (value).isnumberic():
                        value = int(value)
                elif (hasattr(inst, attr) and
                        type(getattr(inst, attr)) is float):
                    idk = args[3].split(".")
                    if idk[0].isnumberic() and idk[1].isnumberic():
                        value = float(value)
                setattr(obj_data[key], attr, value)
                models.storage.save()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
