#!/usr/bin/python3
"""Defines a Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a Rectangle class instance."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle class instance

        Args:
            width (int): Width of the Rectangle instance
            height (int): Height of the Rectangle instance
            x (int): The x position of the Rectangle instance
            y (int): The y position of the Rectangle instance
            id (int): The Id of the Rectangle instance

        Raises:
            TypeError: If width, height, x or, y is not an integer
            ValueError: If width or height <= 0
            ValueError: If x or y < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the Rectangle instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets width of Rectangle instance

        Args:
            value (int): The width of the Rectangle

        Raises:
            TypeError: If value is not an integer
            ValueError: If value <= 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the Rectangle instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets height of Rectangle instance

        Args:
            value (int): The height of the Rectangle

        Raises:
            TypeError: If value is not an integer
            ValueError: If value <= 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Sets/Gets The Rectangle instance x position"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets x position of Rectangle instance

        Args:
            value (int): The x position of the Rectangle

        Raises:
            TypeError: If value is not an integer
            ValueError: If value < 0
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Sets/Gets The Rectangle instance y position"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets x position of Rectangle instance

        Args:
            value (int): The y position of the Rectangle

        Raises:
            TypeError: If value is not an integer
            ValueError: If value < 0
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates and returns the area of the Rectangle instance"""
        return self.width * self.height
