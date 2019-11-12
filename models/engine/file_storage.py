#!/usr/bin/python3

"""
File storage
"""
import json
import os.path


class FileStorage:
    """
    Class for file storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Set objects
        """
        FileStorage.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """
        Save the serializes of objects in JSON file
        """
        dict1 = {}
        for key, value in FileStorage.__objects.items():
            dict1[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="UTF8") as f:
            json.dump(dict1, f)

    def reload(self):
        from models.base_model import BaseModel
        """
        Reload the deserializes the JSON file
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding="UTF8") as f:
                super_dict = json.load(f)
            for key, value in super_dict.items():
                FileStorage.__objects[key] = BaseModel(**value)
