#!/usr/bin/python3
"""BaseModel module"""

from datetime import datetime
import uuid
import models


class BaseModel:
    """BaseModel that defines all common attributes/methods"""
    def __init__(self, *args, **kwargs):
        """A  BaseModel classs"""

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """object str representation"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """dictionary containing all keys/values of __dict__ of the instance"""
        dct = {**self.__dict__}
        dct['__class__'] = self.__class__.__name__
        dct['created_at'] = dct['created_at'].isoformat()
        dct['updated_at'] = dct['updated_at'].isoformat()
        return dct
