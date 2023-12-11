#!/usr/bin/python3
"""
Review Module
Inherits from BaseModel class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class

    Attributes:
        place_id (str): Place.id
        user_id (str): User.id
        text (str): the review
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Init method for Review class"""
        super().__init__(*args, **kwargs)
