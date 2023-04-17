#!/usr/bin/python3
"""Defines a Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a Square class instance."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square class instance

        Args:
            size (int): Length of sides of the Square instance
            x (int): The x position of the Square instance
            y (int): The y position of the Square instance
            id (int): The Id of the Square instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the representation of the Square instance"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                    self.x,
                                                    self.y,
                                                    self.width)

    @property
    def size(self):
        """Get the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets width and height of the Rectangle instance

        Args:
            value (int): The size of the Rectangle

        Raises:
            TypeError: If value is not an integer
            ValueError: If value <= 0
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns arguments passed to the program to the Square instance

        Args:
            *args:  Variable number of arguments, expected to contain integers
                    where:
                        1st argument is the id attribute
                        2nd argument is the size attribute
                        3rd argument is the x attribute
                        4th argument is the y attribute

            **kwargs: Variable number of Key/value arguments
        """
        if args and len(args) != 0:
            iteration = 0
            for arg in args:
                if iteration == 0:
                    self.id = arg
                elif iteration == 1:
                    self.size = arg
                elif iteration == 2:
                    self.x = arg
                elif iteration == 3:
                    self.y = arg
                iteration += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns dictionary representation of the Square instance"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }