#!/usr/bin/python3

"""
File storage
"""
import json
import os.path
from models.base_model import BaseModel

class FileStorage():
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
        key = str(obj.__class__.__name__) + '.' + str(obj.id)
        value = obj.to_dict()
        self.__objects[key] = value
        print(self.__objects)


    def save(self):
        """
        Save the serializes of objects in JSON file
        """
        dict1 = {}
        for key, val in self.__objects.items():
            dict1[key] = str(val)

        print(dict1)
        with open(self.__file_path, 'w', encoding="UTF8") as f:
            json.dump(dict1, f)

    def reload(self):
        """
        Reload the deserializes the JSON file
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                __objects = json.load(f)
