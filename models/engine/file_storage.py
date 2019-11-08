#!/usr/bin/python3

"""
File storage
"""
import json
import os.path
from models.base_model import BaseModel

class FileStorage(BaseModel):
    """
    Class for file storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Set objects
        """
        print(type(obj))
        print("Este es ", obj)

        self.__objects[obj['__class__'] + '.' + obj['id']] = obj

    def save(self):
        """
        Save the serializes of objects in JSON file
        """
        with open(self.__file_path, 'w') as f:
            dict1 = self.to_dict()
            dict1 = json.dumps(dict1)
            f.write(dict1)

    def reload(self):
        """
        Reload the deserializes the JSON file
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                data = f.read()
                print(data)
