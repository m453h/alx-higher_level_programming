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
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Sets/Gets the Rectangle instance width"""
        return self.__width

    @property
    def height(self):
        """Sets/Gets the Rectangle instance height"""
        return self.__height

    @property
    def x(self):
        """Sets/Gets The Rectangle instance x position"""
        return self.__x

    @property
    def y(self):
        """Sets/Gets The Rectangle instance y position"""
        return self.__y
