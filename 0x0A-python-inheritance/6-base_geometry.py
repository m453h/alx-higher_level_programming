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
