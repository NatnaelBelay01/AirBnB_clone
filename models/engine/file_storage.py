#!/usr/bin/python3
"""the storage engine"""
import json
from models.base_model import BaseModel


class FileStorage:
    """the class that does the storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dict"""
        return FileStorage.__objects

    def new(self, obj):
        """sets the __objects"""
        nam = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(nam, obj.id)] = obj

    def save(self):
        """serializes the objects"""
        obj = FileStorage.__objects
        ob_dic = {}
        for i in obj.keys():
            ob_dic[i] = obj[i].to_dict()
        try:
            with open(FileStorage.__file_path, "w") as fp:
                json.dump(ob_dic, fp)
        except FileNotFoundError:
            return

    def reload(self):
        """deserializes a json file"""
        try:
            with open(FileStorage.__file_path) as fp:
                data = json.load(fp)
                for i in data.values():
                    nam = i["__class__"]
                    del i["__class__"]
                    self.new(eval(nam)(**i))
        except FileNotFoundError:
            return
