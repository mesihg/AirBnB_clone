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
        arg = parse(line)
        obj_data = models.storage.all()
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in classes:
            print("** class doesn't exist **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg[0], arg[1]) not in obj_data.keys():
            print("** no instance found **")
            return False
        if len(arg) == 2:
            print("** attribute name missing **")
            return False
        if len(arg) == 3:
            try:
                type(eval(arg[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(arg) == 4:
            obj = obj_data["{}.{}".format(arg[0], arg[1])]
            if arg[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg[2]])
                obj.__dict__[arg[2]] = valtype(arg[3])
            else:
                obj.__dict__[arg[2]] = arg[3]
        elif type(eval(arg[2])) == dict:
            obj = obj_data["{}.{}".format(arg[0], arg[1])]
            for k, v in eval(arg[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
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
