#!/usr/bin/python3
"""
Base Model
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        init method
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == 'my_number':
                    self.my_number = value
                if key == 'name':
                    self.name = value
                if key == 'id':
                    self.id = value

    def __str__(self):
        """
        str method
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        cpy_dict = dict(self.__dict__)
        cpy_dict['__class__'] = self.__class__.__name__
        cpy_dict['created_at'] = self.created_at.isoformat()
        cpy_dict['updated_at'] = self.updated_at.isoformat()
        return (cpy_dict)
