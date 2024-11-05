# models/base.py

class Base:
    """
    Base class for managing `id` attribute in future classes.
    This helps centralize `id` management, avoiding repetitive code.
    """
    # Private class attribute to count objects created from Base class
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.
        
        Parameters:
        id (int): Optional. If provided, this value is used as the instance's id.
                  If not provided, an automatic id is assigned.
        """
        if id is not None:
            # Assign the given id if provided
            self.id = id
        else:
            # Increment the count and assign it to the instance id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
