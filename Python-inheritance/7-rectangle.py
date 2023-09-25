"""
This is module for class Basegeometry.
"""

BaseGeometry = __import__('6-rectangle').BaseGeometry


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

    def area(self):
        """ returns the area of the object."""
        return self.__width * self.__height

    def __str__(self):
        """ str magic method"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)