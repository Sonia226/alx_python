"""
This's a square module.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This is a square class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        This is the initialization method
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str magic method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        getter method for size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter method for size.
        """
        self.width = value
        self.width = value