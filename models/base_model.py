#!/usr/bin/python3
"""
Base Model
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Class for Base Model that is parent of all clasess
    """

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
            kwargs['created_at'] = datetime.strptime(
                kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(
                kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            for key, value in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, value)

    def __str__(self):
        """
        str method
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        """
        representation method
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
        Update the date
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dict of the inst
        """
        cpy_dict = dict(self.__dict__)
        cpy_dict['__class__'] = self.__class__.__name__
        cpy_dict['created_at'] = self.created_at.isoformat()
        cpy_dict['updated_at'] = self.updated_at.isoformat()
        return (cpy_dict)
