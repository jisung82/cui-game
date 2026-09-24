from cui_game.game import Game


def test_new_game_defaults() -> None:
    game = Game.new_game()

    assert game.state.player.hp == 100
    assert game.state.player.gold == 0
    assert game.state.turn == 1


def test_wait_advances_turn() -> None:
    game = Game.new_game()

    result = game.handle_command("wait")

    assert result == "You wait. Turn 2."
    assert game.state.turn == 2


def test_quit_stops_game() -> None:
    game = Game.new_game()

    result = game.handle_command("quit")

    assert result == "Goodbye."
    assert game.state.running is False
