#!/usr/bin/python3
"""
State module
Inherits from the BaseModel class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class

    Public class attributes:
        - name (str): Empty in the beginning
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """State instantiation"""
        super().__init__(*args, **kwargs)
