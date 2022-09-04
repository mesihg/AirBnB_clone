#!/usr/bin/python3
"""FileStorage module"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """"FileStorage class constructor"""
        pass

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """update __objects with new object"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects.update({key: obj})

    def save(self):
        """Serialize __objects to json file __file_path"""
        obdata = FileStorage.__objects
        objs = {obj: obdata[obj].to_dict() for obj in obdata.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(objs, f)

    def reload(self):
        """Deserialize the json file back to __objects"""
        if not os.path.exists(FileStorage.__file_path):
            return
        try:
            with open(FileStorage.__file_path, 'r') as f:
                dcts = json.load(f)
                dcts = {key: classes[val["__class__"]](
                    **val) for key, val in dcts.items()}
                FileStorage.__objects = dcts
        except FileNotFoundError:
            return
