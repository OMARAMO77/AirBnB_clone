#!/usr/bin/python3
"""
Module for User class, inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
