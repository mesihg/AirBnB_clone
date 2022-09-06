#!/usr/bin/python3
"""command interpreter console module"""
import cmd
import re
from shlex import split
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


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


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
        arg = parse(line)
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif arg[0] not in classes:
            print("** class doesn't exist **")
        else:
            obj_data = models.storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key in obj_data:
                print(obj_data[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        arg = parse(line)
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            obj_data = models.storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key in obj_data:
                obj_data.pop(key, None)
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        arg = parse(line)
        if len(arg) > 0 and arg[0] not in classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in models.storage.all().values():
                if len(arg) > 0 and arg[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(arg) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_count(self, arg):
        """Count number of instances of a given class"""
        arg = parse(arg)
        count = 0
        for obj in models.storage.all().values():
            if arg[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, line):
        """Updates an instance based on the class name and id:"""
        args = line.split()
        obj_data = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in obj_data:
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

    def do_quit(self, arg):
        'Quit command to exit the program.'
        return True

    def do_EOF(self, arg):
        'Quit command to exit the program.'
        return True

    def emptyline(self):
        """Don't do any thing"""
        pass

    def default(self, arg):
        """Default behavior when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
