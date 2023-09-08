from tiles import Tiles
from board import Board
from player import Player
from computer import Computer
from game_controller import GameController


def test_constructors():
    """Test the constroctor of the GameController class"""
    ts = Tiles(90, 8, 8, 100)
    p = Player(ts)
    c = Computer(ts)
    b = Board(100, 8, 8, ts, p, c)
    gc = GameController(200, b, p, c)

    assert gc.TEXT_POS == 200
    assert gc.board == b
    assert gc.player == p
    assert gc.computer == c
    assert gc.FONTCOLOR == (255, 0, 0)
    assert not gc.game_end
