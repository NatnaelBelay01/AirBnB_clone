#!/usr/bin/python3
"""a city class that inherits from Basemodel """
from models.base_model import BaseModel


class City(BaseModel):
    """the city class"""
    state_id = ""
    name = ""
