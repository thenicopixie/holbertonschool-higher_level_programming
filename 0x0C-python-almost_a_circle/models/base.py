#!/usr/bin/python3
"""Module for base class Base"""
import json


class Base:
    """The Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """A Class constructor to initialize id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of
        list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of
        list_objs to a file"""
        filename = str(cls.__name__) + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                j_list = []
                for i in list_objs:
                    j_list.append(cls.to_dictionary(i))
                f.write(cls.to_json_string(j_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of JSON string
        representation"""
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        #if cls.__name__ == "Rectangle":
         #   dummy = cls(width=1, height=1)
        #elif cls.__name__ == "Square":
         #   dummy = cls(size=1)
        dummy = cls(1, 1)
        cls.update(dictionary)
        return dummy

#    @classmethod
 #   def load_from_file(cls):
  #      """Returns a list of instances"""
   #     filename = str(cls.__name__) + ".json"
    #    i_list = []
       # j_list = []
        #if filename is None:
      #      return i_list
     #   else:
         #   with open(filename, mode="r", encoding="utf-8") as f:
          #      i_list = cls.from_json_string(f.read())
           #     for j in i_list:
            #        j_list.append(cls.create(**j))
             #   return j_list
