#!/usr/bin/python3

"""defines Base class for future use."""


class Base:
    """
    Base class for managing `id` attribute in future classes.
    This helps centralize `id` management, avoiding repetitive code.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Parameters:
        id (int): Optional. If provided,
        this value is used as the instance's id.
                  If not provided, an automatic id is assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
