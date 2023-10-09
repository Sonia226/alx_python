"""
This is a module for class Base
"""

from models.base import Base
"""
This imports the class base
"""


class Rectangle(Base):
    """
    This is class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This is the initialization method
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """
        getter method for width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method for width.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        getter method for height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method for height.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        getter method for x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter method for x.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        getter method for y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter method for y.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        This is an area method
        """
        return self.__height * self.__width

    def display(self):
        """
        This is a display method.
        """
        for row in range(self.y):
            print()
        else:
            for row in range(self.height):
                for column in range(self.x):
                    print(" ", end="")
                else:
                    for column in range(self.width):
                        print("#", end="")
                    else:
                        print()

    def __str__(self):
        """ str magic method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        This method assigns an argument
        """
        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "width":
                self.width = value
            elif key == "height":
                self.height = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value

        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]