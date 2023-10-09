"""
This is function module .
"""
def is_same_class(obj, a_class):
        """
        This function returns true/false if obj is exactly an instance of the specified class.
        """
        return isinstance(obj, a_class) and type(obj) == a_class