#!/usr/bin/python3
"""Defines a Base class."""
import json
import csv
import turtle


class Base:
    """
    Represent a Base class instance.

    Attributes:
        __nb_objects (int): The number of Base instances.

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): The id of the new Base instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): The list of dictionaries.

        Return:
            (string): JSON representation of list_dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): The list of instances who inherits from Base.

        Return:
            (string): JSON representation of list_dictionaries.
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__+".json"
        current_json_list = []

        for obj in list_objs:
            current_json_list.append(obj.to_dictionary())

        output = cls.to_json_string(current_json_list)

        with open(filename, 'w') as file:
            file.write(output)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON string representation json_string.

        Args:
            json_string (str): String representing a list of dictionaries.

        Returns:
            (list): The list represented by json_string.
        """
        if json_string is None or json_string == "[]" or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance of a class with all attributes set.

        Args:
            **dictionary (dict): Dictionary with attributes to initialize.

        Returns:
            (obj): The instance of a Rectangle or Square
                   with attributes in **dictionary.
        """
        if dictionary is not None and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)

            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns an instance of a class with all attributes set.

        Args:
            **dictionary (dict): Dictionary with attributes to initialize.

        Returns:
            (obj): The instance of a Rectangle or Square
                   with attributes in **dictionary.
        """
        instances = []
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as input_file:
                json_string = input_file.read()

                if json_string:
                    json_list = Base.from_json_string(json_string)
                    for dictionary in json_list:
                        instance = cls.create(**dictionary)
                        instances.append(instance)
        except FileNotFoundError:
            pass

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes the CSV string representation of list_objs to a file.

        Args:
            list_objs (list): The list of instances who inherits from Base.

        Return:
            (string): CSV representation of list_dictionaries.
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__+".csv"
        current_csv_list = []

        for obj in list_objs:
            current_csv_list.append(obj.to_dictionary())

        with open(filename, 'w') as file:
            if cls.__name__ == "Rectangle":
                headers = ["id", "width", "height", "x", "y"]
            else:
                headers = ["id", "size", "x", "y"]
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writerows(current_csv_list)

    @classmethod
    def load_from_file_csv(cls):
        """
        Returns an instance of a class with all attributes set.

        Returns:
            (obj): The instance of a Rectangle or Square
                   with attributes in **dictionary.
        """
        instances = []
        filename = str(cls.__name__) + ".csv"
        try:
            with open(filename, "r") as input_file:
                if cls.__name__ == "Rectangle":
                    headers = ["id", "width", "height", "x", "y"]
                else:
                    headers = ["id", "size", "x", "y"]

                csv_dict = csv.DictReader(input_file, fieldnames=headers)

                for dictionary in csv_dict:
                    new_dict = {}

                    for key, value in dictionary.items():
                        new_dict[key] = int(value)

                    instance = cls.create(**new_dict)
                    instances.append(instance)
        except FileNotFoundError:
            pass

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares.

        Args:
            list_rectangles (list): List of Rectangle instances to draw.
            list_squares (list): List of Square instances to draw.
        """
        ttl = turtle.Turtle()
        ttl.screen.bgcolor("#ffffff")
        ttl.pensize(3)
        ttl.shape("classic")

        ttl.color("#e74c3c")
        for rectangle in list_rectangles:
            ttl.showturtle()
            ttl.up()
            ttl.goto(rectangle.x, rectangle.y)
            ttl.down()
            for i in range(2):
                ttl.forward(rectangle.width)
                ttl.left(90)
                ttl.forward(rectangle.height)
                ttl.left(90)
            ttl.hideturtle()

        ttl.color("#2980b9")

        for square in list_squares:
            ttl.showturtle()
            ttl.up()
            ttl.goto(square.x, square.y)
            ttl.down()
            for i in range(4):
                ttl.forward(square.width)
                ttl.left(90)
            ttl.hideturtle()

        turtle.exitonclick()
