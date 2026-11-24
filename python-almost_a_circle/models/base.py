#!/usr/bin/python3
"""
Module defining the Base class for all models in the project.

This module provides ID management as well as JSON and CSV serialization
and deserialization methods for Base subclasses.
"""
import csv
import json
import os


class Base:
    """Base class for managing object IDs and file serialization."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base instance with an explicit or auto-assigned ID."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = "{}.json".format(cls.__name__)
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by the JSON string json_string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set from dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from <Class name>.json."""
        filename = "{}.json".format(cls.__name__)
        if not os.path.exists(filename):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            list_dicts = cls.from_json_string(f.read())
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to a CSV file."""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if list_objs is None or len(list_objs) == 0:
                return
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height,
                                     obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of objects from a CSV file."""
        filename = "{}.csv".format(cls.__name__)
        if not os.path.exists(filename):
            return []
        instances = []
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                vals = [int(x) for x in row]
                if cls.__name__ == "Rectangle":
                    data = {"id": vals[0], "width": vals[1],
                            "height": vals[2], "x": vals[3], "y": vals[4]}
                elif cls.__name__ == "Square":
                    data = {"id": vals[0], "size": vals[1],
                            "x": vals[2], "y": vals[3]}
                instances.append(cls.create(**data))
        return instances
