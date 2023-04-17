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
