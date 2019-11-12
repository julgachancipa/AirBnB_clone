#!/usr/bin/python3
"""
Unittest for base
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelClass(unittest.TestCase):
    """
    Test Base Classes
    """
    def test_right_cases(self):
        """
        right cases
        """
        my_model = BaseModel()
        my_model.name = "Holbi"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "Holbi")
        self.assertEqual(my_model.my_number, 89)
        self.assertEqual(my_model.__class__.__name__, "BaseModel")
        self.assertEqual(isinstance(my_model.created_at, datetime), True)
        self.assertEqual(isinstance(my_model.updated_at, datetime), True)
