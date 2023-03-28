#!/usr/bin/python3
"""Define class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new instance of Square class.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Return the size of the current square instance."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the current square instance."""
        return (self.__size * self.__size)
