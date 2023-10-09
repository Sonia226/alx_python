"""
This is module for class Square.
"""

Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """
    This a class Square.
    """

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ returns the area of the object."""
        return self.__size * self.__size