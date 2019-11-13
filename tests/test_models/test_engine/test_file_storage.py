#!/usr/bin/python3
"""
Unittest for file_storage
"""
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test File Storage
    """
    def test_right_cases(self):
        """
        right cases
        """
        my_object = FileStorage()
        self.assertEqual(my_object.all, my_object.__objects)
