#!/usr/bin/python3
"""
Module that defines the FileStorage class.

-> The class is responsible for serializing instances  to a JSON file,
and deserializing JSON files back to instances.
"""
from models.base_model import BaseModel
from models.user import User
import json

clss = {
    "BaseModel": BaseModel,
    "User": User
}
"""clss (dict): dictionary of class objects"""


class FileStorage():
    """
    Class responsible for handling file storage using JSON.

    Private class attributes:
        - `__file_path` (str): path to the JSON file.
        - `__objects` (dict): empty in the beginning.
            stores all objects by <class name>.id
            (ex: BaseModel object with id=12121212,
                the key will be BaseModel.12121212)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the __objects dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        Adds an object to `__objects`.
        with key <class name>.id

        Args:
            obj (object): the object to be added
        """
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects.update({key: obj})

    def save(self):
        """
        Serializes `__objects` to the JSON file
        """
        with open(self.__file_path, 'w') as f:
            if self.__objects is None:
                f.write("{}")
            else:
                serialized = {
                    key: obj.to_dict()
                    for key, obj in self.__objects.items()

                }
                json.dump(serialized, f, indent=2)

    def reload(self):
        """
        Deserializes the JSON file to __objects (if the file exits).
        Otherwise, nothing is done and no exception is raised.
        """
        try:
            with open(self.__file_path, 'r') as f:
                load = json.load(f)
                for k in load:
                    self.__objects[k] = clss[load[k]["__class__"]](**load[k])
        except Exception as e:
            pass
