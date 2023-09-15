""" Class module"""

class Square:
    """A class that represent a Square."""
    
    def __init__(self, size=0):
        """Initializing the size.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size  
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError ("size must be an integer")
        elif value < 0:
            raise ValueError ("size must be >= 0")
    
        self.__size = value

    def area(self):
        area = self.__size * self.__size
        return area