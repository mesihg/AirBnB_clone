#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {"BaseModel": BaseModel,
           "User": User,
           "State": State,
           "City": City,
           "Amenity": Amenity,
           "Place": Place,
           "Review": Review
           }


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects.update({key: obj})

    def save(self):
        objs = {key: val.to_dict() for key, val in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(objs, f)

    def reload(self):

        if not os.path.exists(self.__file_path):
            return
        try:
            with open(self.__file_path, 'r') as f:
                dcts = json.load(f)
                dcts = {key: classes[val["__class__"]](
                    **val) for key, val in dcts.items()}
                self.__objects = dcts
        except Exception as ex:
            print(ex)
