#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represent a Student class instance."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student class instance

        Args:
            first_name (string): The first name of the student instance
            last_name (string): The last name of the student instance
            age (int): The age of the student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return self.__dict__
