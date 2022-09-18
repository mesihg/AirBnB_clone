#!/usr/bin/python3
"""FileStorage module"""
import json
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

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """update __objects with new object"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to json file __file_path"""
        obdata = FileStorage.__objects
        objs = {obj: obdata[obj].to_dict() for obj in obdata.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(objs, f)

    def reload(self):
        """Deserialize the json file back to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                dcts = json.load(f)
                for obj in dcts.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
