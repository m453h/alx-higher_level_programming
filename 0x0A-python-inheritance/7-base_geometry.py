#!/usr/bin/python3
"""Define class BaseGeometry."""


class BaseGeometry:
    """Defines a BaseGeometry class instance."""

    def area(self):
        """
            Defines generic non-implemented area method.

            Raises:
                    Exception: area() is not implemented.

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Validates if value is an integer.

            Args:
                name (str): The name of the parameter.
                value (int): The parameter to validate if is an integer.

            Raises:
                    TypeError: If value is not an integer.
                    ValueError: If value is not greater than 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
