from . import exceptions
from .config import Config, get_default_config
from .game_object import GameObject


class PeaPy:
    """
    The main class of the game engine.
    """

    def __init__(self, config: Config = get_default_config()):
        """
        Construct a new PeaPy game.

        :param config: The configuration to use.
        """

        self.config = config

        self.game_objects: dict[str, GameObject] = {}

    def update(self) -> bool:
        """
        Update the game.

        :return: True if the game should continue, False if the game should end.
        """

        for game_object in self.game_objects.values():  # Loop through all game objects.
            if not game_object.update_():  # Update the game object and check if it should continue.
                return False  # Game should end.

        return True

    def add_game_object(self, game_object: GameObject) -> GameObject:
        """
        Add a game object to the game.

        :param game_object: The game object to add.
        :return: The game object that was added. This allows for the following patterns:
            game_object = game.add_game_object(GameObject()) or
            game.add_game_object(GameObject()).do_something()
        """

        if game_object.name in self.game_objects:
            raise exceptions.game_object.GameObjectAlreadyExists(game_object.name)

        self.game_objects[game_object.name] = game_object
        game_object.init_(self)
        return game_object

    def get_game_object(self, name: str) -> GameObject:
        """
        Get a game object by name.

        :param name: The name of the game object to get.
        :return: The game object.
        """

        if name not in self.game_objects:
            raise exceptions.game_object.GameObjectDoesNotExist(name)

        return self.game_objects[name]

    def get_game_objects(self) -> dict[str, GameObject]:
        """
        Get all game objects.

        :return: A dictionary of all game objects.
        """

        return self.game_objects

    def remove_game_object(self, name: str):
        """
        Remove a game object from the game.

        :param name: The name of the game object to remove.
        """

        if name not in self.game_objects:
            raise exceptions.game_object.GameObjectDoesNotExist(name)

        del self.game_objects[name]

    def __repr__(self):
        return f"{self.__class__.__name__}()"
