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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        Args:
            attrs (list): List of strings containing attribute names

        Return (dict):  Dictionary that contains details of the Student
        """

        student_dict = {}

        if attrs is not None:
            for attribute in attrs:
                if hasattr(self, attribute):
                    student_dict[attribute] = getattr(self, attribute)
        else:
            student_dict = self.__dict__

        return student_dict
