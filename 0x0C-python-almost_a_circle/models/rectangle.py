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

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        for y in range(self.y):
            print("")

        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print('#', end="")
            if i != self.height - 1:
                print("")
        print("")

    def __str__(self):
        """Returns the representation of the Rectangle instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """
        Assigns arguments passed to the program to the Rectangle instance

        Args:
            *args:  Variable number of arguments, expected to contain integers
                    where:
                        1st argument is the id attribute
                        2nd argument is the width attribute
                        3rd argument is the height attribute
                        4th argument is the x attribute
                        5th argument is the y attribute

            **kwargs: Variable number of Key/value arguments
        """
        if args and len(args) != 0:
            iteration = 0
            for arg in args:
                if iteration == 0:
                    self.id = arg
                elif iteration == 1:
                    self.width = arg
                elif iteration == 2:
                    self.height = arg
                elif iteration == 3:
                    self.x = arg
                elif iteration == 4:
                    self.y = arg
                iteration += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns dictionary representation of the Rectangle instance"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
