#!/usr/bin/python3
"""
City module
Inherits from the BaseModel class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class

    Public class attributes:
        - name (str): Empty in the beginning
    """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """City instantiation"""
        super().__init__(*args, **kwargs)
