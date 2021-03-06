#!/usr/bin/python3
"""
Unittest for user
"""
import unittest
from datetime import datetime
from models.user import User


class TestBaseModelClass(unittest.TestCase):
    """
    Test User
    """
    def test_right_cases(self):
        """
        right cases
        """
        self.assertIsNotNone(User.__doc__)
        my_model = User()
        my_model.name = "Holbi"
        my_model.my_number = 89
        my_model.first_name = "Juli"
        my_model.last_name = "Gacast"
        my_model.email = "jul@ga.com"
        my_model.password = "root"
        self.assertTrue(hasattr(my_model, "name"))
        self.assertTrue(hasattr(my_model, "my_number"))
        self.assertTrue(hasattr(my_model, "first_name"))
        self.assertTrue(hasattr(my_model, "last_name"))
        self.assertTrue(hasattr(my_model, "email"))
        self.assertTrue(hasattr(my_model, "password"))
        self.assertEqual(my_model.name, "Holbi")
        self.assertEqual(my_model.my_number, 89)
        self.assertEqual(my_model.__class__.__name__, "User")
        self.assertEqual(my_model.first_name, "Juli")
        self.assertEqual(my_model.last_name, "Gacast")
        self.assertEqual(my_model.email, "jul@ga.com")
        self.assertEqual(my_model.password, "root")
        self.assertTrue(isinstance(my_model.created_at, datetime))
        self.assertTrue(isinstance(my_model.updated_at, datetime))
        my_model.save()
        self.assertTrue(isinstance(my_model.updated_at, datetime))
        my_model_dict = my_model.to_dict()
        self.assertIs(type(my_model_dict), dict)

if __name__ == "__main__":
    unittest.main()
