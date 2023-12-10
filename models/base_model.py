#!/usr/bin/python3
"""
Module that defines the BaseModel class.

Provides a base class, that serves as a foundation for other classes.
It defines common attributes and methods to be inherited
"""
from datetime import datetime
from uuid import uuid4

d_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """
    Base class for other classes to inherit from.
    Defines common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Class instantiation method.

        Public instance attributes:
            - `id` (str): Unique identifier.
            - `created_at` (datetime): Instance creation timestamp.
            - `updated_at` (datetime): Instance update timestamp.
        """
        if kwargs:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(val, d_format))
                    else:
                        setattr(self, key, val)
        else:
            from models import storage
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
            storage.save()

    def __str__(self):
        """
        Human-readable string representation

        Returns:
            Formatted str: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute 'update_at'
        with the current datetime.
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of `__dict__` of
        the instance, + class name + string representation of the dates.

        Returns:
            dict: Dictionary representation of the instance.
        """
        result_dict = self.__dict__.copy()
        result_dict['__class__'] = self.__class__.__name__
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()
        return result_dict
