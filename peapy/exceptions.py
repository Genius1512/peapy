class Component:
    class ComponentAlreadyExists(Exception):
        """
        Raised when a component is added to a game object that already has a component of the same type.
        """

    class ComponentDoesNotExist(Exception):
        """
        Raised when a component is requested from a game object that does not have a component of the same type.
        """


class GameObject:
    class GameObjectAlreadyExists(Exception):
        """
        Raised when trying to create a game object that already exists.
        """

    class GameObjectDoesNotExist(Exception):
        """
        Raised when trying to get a game object that does not exist.
        """


class PeaPy:
    pass


class Config:
    class AttributeNotFound(Exception):
        """
        Raised when trying to get an attribute of a config object that does not exist.
        """
