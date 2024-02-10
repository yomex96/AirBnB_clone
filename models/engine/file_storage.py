#!/usr/bin/python3
"""
The class FileStorage is a class that define the new dictionary of the class
"""


from models.base_model import BaseModel
import json
import os
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    All the instance used listed:
        all(self):
        new(self, obj):
        save(self):
        reload(self):
    """

    def __init__(self):
        """
        Function - all(self):
            return the object

            Object:
                nothing

            Return:
                object
        """
        self.__file_path = "file.json"
        self.__objects = dict()

    def all(self):
        """
        Function - all(self):
            return the object

            Object:
                nothing

            Return:
                object
        """
        return(self.__objects)

    def new(self, obj):
        """
        Function - new(self, obj):
            add new object to the dict

            Object:
                copy(str): the dictionary of the file

            Return:
                nothing
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Function - save(self):
            save the new dictionary

            Object:
                file(str): the name of wherethe file is
                dict3(dict): the new dictionary

            Return:
                nothing
        """
        with open(self.__file_path, mode="w", encoding="utf-8") as my_file:
            __dic = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(__dic, my_file)

    def reload(self):
        """
        Function - reload(self):
            reload a new dictionary

            Object:
                file(str): the name of wherethe file is
                FileStorage.__objects(dict): the new dictionary

            Return:
                nothing
        """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                dic_to_dic = json.load(f)
                for val in dic_to_dic.values():
                    self.new(eval(val['__class__'])(**val))
        except Exception:
            pass
