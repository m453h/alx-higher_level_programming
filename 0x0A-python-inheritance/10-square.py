#!/usr/bin/python3
"""Define class Square, inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a Square class instance."""

    def __init__(self, size):
        """
            Intialize a new Square instance.

            Args:
                size (int): The length of one side of the Square instance.
        """
        self.integer_validator("size", size)
        self.__size = size


    def area(self):
        """ Returns the area of the current Square instance. """
        return self.__size * self.__size

    def __str__(self):
        """ Returns the representation of the Rectangle instance."""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)