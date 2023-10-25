#!/usr/bin/python3
""" define a class"""


class Square():
    """the class"""
    def __init__(self, __size=0) -> None:
        if type(__size) != int:
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = __size
