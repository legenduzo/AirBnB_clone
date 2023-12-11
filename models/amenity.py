#!/usr/bin/python3
"""
Amenity module
Inherits from the BaseModel class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class

    Public class attributes:
        - name (str): Empty in the beginning
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Amenity instantiation"""
        super().__init__(*args, **kwargs)
