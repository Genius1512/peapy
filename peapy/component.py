class Component:
    """
    The component class.
    Components are used to add functionality to game objects.
    """

    def __init__(self):
        self.game_object = None

    def init_(self, game_object: object):
        """
        Used by PeaPy to initialize the component.
        Don't call this manually or override it.
        Use the init() method instead.

        :param game_object: The game object.
        """

        self.game_object = game_object

        self.init()

    def init(self):
        """
        Called when the component is added to the game object.
        """

    def update_(self) -> bool:
        """
        This method is called by PeaPy to update the component.
        Don't call this manually or override it.
        Use the update() method instead.

        :return: True if the game should continue, False if the game should end.
        """

        return self.update()

    def update(self) -> bool:
        """
        Update the game.

        :return: True if the game should continue, False if the game should end.
        """

        return True

    def __repr__(self):
        return f"{self.__class__.__name__}()"
