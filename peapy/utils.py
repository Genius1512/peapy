from .peapy import PeaPy


def tree(game: PeaPy):
    """
    Print a tree of game objects and their components

    :param game: The peapy instance.
    """

    for name, game_object in game.game_objects.items():
        print(f"{name}")
        for component_name, component in game_object.components.items():
            print(f"\t{component_name}")
