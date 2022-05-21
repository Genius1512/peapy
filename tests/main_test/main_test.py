import peapy


def main():
    game = peapy.PeaPy()

    player = game.add_game_object(peapy.GameObject("Player"))
    player.add_component(peapy.Transform(
        100,
        100,
        50,
        50
    ))

    while game.update():
        pass


if __name__ == "__main__":
    main()
