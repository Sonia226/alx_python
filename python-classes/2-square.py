''' Class module'''

class Square:
    '''A class that represent a Square.'''
    
    def __init__(self, size=0):
        '''Initializing the size.
        
        Args:
            size (int): The size of the square.
        '''
        if type(size) is not int:
            raise TypeError ("size must be an integer")
        elif size < 0:
            raise ValueError ("size must be >= 0")
    
        self.__size = size
    
    def area(self):
        area = self.__size * self.__size
        return area