class GameObjectAlreadyExists(Exception):
    """
    Raised when trying to create a game object that already exists.
    """


class GameObjectDoesNotExist(Exception):
    """
    Raised when trying to get a game object that does not exist.
    """