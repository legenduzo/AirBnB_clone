#!/usr/bin/python3
"""Package file

Used to reload objects from json file

Attributes:
    storage (FileStorage): Instance of file storage class
"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
