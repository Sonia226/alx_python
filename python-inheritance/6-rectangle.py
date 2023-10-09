"""
This is module for class Basegeometry.
"""

BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is a class Rectangle
    """

    def __init__(self, width, height):
        """
        This is an integer validator method
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height