#!/usr/bin/python3
"""Defines the Basemodel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents BaseModel for the HBnB project"""

    def __innit__(self, *args, **kwargs):
        """Initialize new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str =(uuid())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)
    def save(self):
        """Update updated_at to current datetime."""
        self.updated_at == datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return dictionary for BaseModel instance.

        Has key/value oair __class__ representing 
        the object's class name.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print representation of BaseModel."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
