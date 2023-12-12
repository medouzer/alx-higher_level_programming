#!/usr/bin/python3
""" the unit tests for square """
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class SquareTestCase(unittest.TestCase):
    """ this is the class for square test """

    def setUp(self):
        """
        Resets id 
        """
        Base._Base__nb_objects = 0

    def test_square_id_increment(self):
        pass


if __name__ == '__main__':
    unittest.main()
