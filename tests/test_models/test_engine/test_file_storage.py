#!/usr/bin/python3
"""
Unittest for file_storage
"""
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """
    Test File Storage
    """
    def test_right_cases(self):
        """
        right cases
        """
        my_storage = FileStorage()
        my_dict = my_storage.all()
        self.assertIs(type(my_dict), dict)
