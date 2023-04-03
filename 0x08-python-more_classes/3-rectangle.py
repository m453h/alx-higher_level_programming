#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle instance."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance

        Args:
            width (int): Width of the rectangle instance
            height (int): Height of the rectangle instance
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve rectangle width"""
        return self.__width

    @property
    def height(self):
        """retrieve rectangle height"""
        return self.__height

    @width.setter
    def width(self, value):
        """set the width of the rectangle

        Args:
            value: Width of the rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """set the height of the rectangle

        Args:
            value: Height of the rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return the area of the rectangle instance"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle instance"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """Return the printable representation of the Rectangle instance"""
        if self.width == 0 or self.height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append('#')
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)
