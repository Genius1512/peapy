import peapy


def main():
    game = peapy.PeaPy()

    player = game.add_game_object(peapy.GameObject("Player"))
    player.add_component(peapy.Component())

    while game.update():
        pass


if __name__ == "__main__":
    main()
