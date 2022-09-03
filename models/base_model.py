#!/usr/bin/python
"""A base model for all the objects"""


from datetime import datetime
import uuid
import models


class BaseModel:
    """the base class"""

    def __init__(self, *args, **kwargs):
        """initializes everything"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        formatt = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i in ("created_at", "updated_at"):
                    self.__dict__[i] = datetime.strptime(j, formatt)
                else:
                    self.__dict__[i] = j
        else:
            models.storage.new(self)

    def save(self):
        """updates the updated_at"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary representation"""
        rep = self.__dict__.copy()
        rep["created_at"] = self.created_at.isoformat()
        rep["updated_at"] = self.updated_at.isoformat()
        rep["__class__"] = str(self.__class__.__name__)
        return rep

    def __str__(self):
        """Returns a printable"""
        nam = self.__class__.__name__
        return "[{}] ({}) {}".format(nam, self.id, self.__dict__)
