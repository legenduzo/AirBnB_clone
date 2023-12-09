#!/usr/bin/python3
"""
Module that defines the `User` class that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class

    Public class attributes:
        - `email` (str)
        - `password` (str)
        - `first_name` (str)
        - `last_name` (str)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """User Instantiation"""
        super().__init__(*args, **kwargs)
