#!/usr/bin/python3
"""Define class Rectangle, inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a Rectangle class instance."""

    def __init__(self, width, height):
        """
            Intialize a new Rectangle instance.

            Args:
                width (int): The width of the new Rectangle instance.
                height (int): The height of the new Rectangle instance.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns the area of the current Rectangle instance. """
        return self.__width * self.__height

    def __str__(self):
        """ Prints and Return the representation of the current Rectangle instance."""
        description = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return description