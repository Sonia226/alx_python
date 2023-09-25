"""
This is function module .
"""
def inherits_from(obj, a_class):
        """
        This returns True if the obj is an instance of a
         class that inherited(directly or indirectly) from the specified 
         class: else False
        """
        return issubclass(type(obj), a_class) and type(obj) is not a_class