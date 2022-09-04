#!/usr/bin/python3
"""a class that inherits from base"""
from models.base_model import BaseModel


class User(BaseModel):
    """The class user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
