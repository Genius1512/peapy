class ComponentAlreadyExists(Exception):
    """
    Raised when a component is added to a game object that already has a component of the same type.
    """


class ComponentDoesNotExist(Exception):
    """
    Raised when a component is requested from a game object that does not have a component of the same type.
    """