import os
import re
from argparse import ArgumentParser, Namespace


def camel_to_snake(string: str) -> str:
    """
    Converts a camel case string to snake case.

    :param string: The camel case string.
    :return: The snake case string.
    """

    return re.sub(r"(?<!^)(?=[A-Z])", "_", string).lower()


class Templates:
    MAIN = """import peapy
    

def main():
    game = peapy.PeaPy()
    
    while game.update():
        pass
        
        
if __name__ == "__main__":
    main()
"""

    GAME_OBJECT = """import peapy
    

class {name}(peapy.GameObject):
    def __init__(self, name: str):
        super().__init__(name)
        
    def init(self):  # Called when the GameObject is added to a PeaPy instance.
        pass
        
    def update(self):  # Called every frame.
        pass
"""

    COMPONENT = """import peapy
    
    
class {name}(peapy.Component):
    def __init__(self):
        super().__init__()
        
    def init(self):  # Called when the Component is added to a GameObject.
        pass
        
    def update(self):  # Called every frame.
        pass
"""


def parse_args() -> Namespace:
    parser = ArgumentParser(description="PeaPy's command line interface.")

    parser.add_argument(
        "-n",
        "--new",
        required=False,
        type=bool,
        help="Create a new project.",
    )

    parser.add_argument(
        "-g",
        "--game-object",
        required=False,
        help="Create a new game object.",
    )

    parser.add_argument(
        "-c",
        "--component",
        required=False,
        help="Create a new component.",
    )

    return parser.parse_args()


def create_project():
    print("Creating project...")

    os.mkdir("assets")
    os.mkdir("assets/images")
    os.mkdir("assets/sounds")

    with open("main.py", "w") as f:
        f.write(Templates.MAIN)

    print("Project created.")


def create_game_object(name: str):
    print("Creating game object...")

    with open(f"{camel_to_snake(name)}.py", "w") as f:
        f.write(Templates.GAME_OBJECT.format(name=name))

    print(f"Game object created in {camel_to_snake(name)}.py")


def create_component(name: str):
    print("Creating component...")

    with open(f"{camel_to_snake(name)}.py", "w") as f:
        f.write(Templates.COMPONENT.format(name=name))

    print(f"Component created in {camel_to_snake(name)}.py")


def main():
    args = parse_args()

    if args.new:
        create_project()

    if args.game_object:
        create_game_object(args.game_object)

    if args.component:
        create_component(args.component)


if __name__ == '__main__':
    main()
