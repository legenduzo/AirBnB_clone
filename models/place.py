#!/usr/bin/python3
"""
Place module
Defines the Place class and inherits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class. Used to represent a place on Airbnb

    Public class attributes:
        city_id (str): City.id
        user_id (str): User.id
        name (str): place name
        description (str): place description
        number_rooms (int): number of rooms
        number_bathrooms (int): number of baths
        max_guest (int): max guests
        price_by_night (int): price per night
        latitude (float): latitude
        longitude (float): longitude
        amenity_ids (list of str): list of Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Init method for Place class"""
        super().__init__(*args, **kwargs)
