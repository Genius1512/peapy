from peapy.component import Component
from peapy.exceptions import Component as exceptions


class GameObject:
    """
    The GameObject class is the base class for all game objects.
    GameObjects are used to represent things in the game world (for example the Player).
    """

    def __init__(self, name: str):
        """
        Construct a new GameObject.

        :param name: The name of the game object.
        """

        self.name = name

        self.peapy = None

        self.components: dict[str, Component] = {}

    def init_(self, peapy: object):
        """
        Used by PeaPy to initialize the game object.
        Don't call this manually or override it.
        Use the init() method instead.

        :param peapy: The PeaPy instance.
        """

        self.peapy = peapy

        self.init()

    def init(self):
        """
        Called when the game object is added to the game.
        """

    def update_(self) -> bool:
        """
        This method is called by PeaPy to update the game object.
        Don't call this manually or override it.
        Use the update() method instead.

        :return: True if the game should continue, False if the game should end.
        """

        for component in self.components.values():  # Loop through all components.
            if (
                not component.update()
            ):  # Update the component and check if it should continue.
                return False  # Game should end.

        return self.update()

    def update(self) -> bool:
        """
        Update the game object. This method is called every frame.

        :return: True if the game should continue, False if the game should end.
        """

        return True

    def add_component(self, component: Component) -> Component:
        """
        Add a component to the game object.

        :param component: The component to add.
        :return: The component that was added. This allows for the following patterns:
            component = game_object.add_component(Component()) or
            game_object.add_component(Component()).do_something()
        """

        if component.__class__.__name__ in self.components:
            raise exceptions.ComponentAlreadyExists(component.__class__.__name__)

        self.components[component.__class__.__name__] = component
        component.init_(self)
        return component

    def get_component(self, name: str) -> Component:
        """
        Get a component by name.

        :param name: The name of the component to get.
        :return: The component.
        """

        if name not in self.components:
            raise exceptions.ComponentDoesNotExist(name)

        return self.components[name]

    def get_components(self) -> dict[str, Component]:
        """
        Get all components.

        :return: A dictionary of all components.
        """

        return self.components

    def remove_component(self, name: str):
        """
        Remove a component from the game object.

        :param name: The name of the component to remove.
        """

        if name not in self.components:
            raise exceptions.ComponentDoesNotExist(name)

        del self.components[name]

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"
