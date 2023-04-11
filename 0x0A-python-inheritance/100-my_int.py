#!/usr/bin/python3

""" Defines MyInt class. """


class MyInt(int):
    """ Defines MyInt class instance. """

    def __eq__(self, value):
        """ Defines == operator to behave as the != operator """
        return super().__ne__(value)

    def __ne__(self, value):
        """ Defines != operator to behave as the == operator """
        return super().__eq__(value)
