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
        return "[Square] ({}) {}/{} - {}/{}".format(self.id,
                                                    self.x,
                                                    self.y,
                                                    self.width,
                                                    self.height)

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
