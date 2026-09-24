from .game import Game


def main() -> None:
    game = Game.new_game()
    game.run()


if __name__ == "__main__":
    main()
