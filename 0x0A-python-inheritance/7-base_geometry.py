#!/usr/bin/python3
""" Integer validator """


class BaseGeometry:
    """ geometry class """
    pass

    def area(self):
        """ area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate the integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
