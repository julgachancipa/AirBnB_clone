#!/usr/bin/python3
"""
class Review that inherits from Base Model
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review
    """
    place_id = ''
    user_id = ''
    text = ''
