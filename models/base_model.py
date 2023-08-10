#!/usr/bin/python3
""" This will create the base code for the Airbnb clone """
import uuid

class BaseModel:
    """ The base of all other model """

    def __init__(self, id, created_at, updated_at):
        """
        id is generated woth the uuid random unique 
        value generatir and it is converted to a string
        created_at is the date of creation.
        updated_at is the date of each modification.
        """
