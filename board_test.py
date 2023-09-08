from tiles import Tiles
from board import Board
from player import Player
from computer import Computer


def test_constructor():
    """Test for the construtor of the Board class"""
    ts = Tiles(90, 8, 8, 100)
    p = Player(ts)
    c = Computer(ts)
    b = Board(100, 8, 8, ts, p, c)

    assert b.SIZE == 100
    assert b.ROWS == 8
    assert b.COLUMNS == 8
    assert b.player == p
    assert b.computer == c
    assert b.tiles == ts
    assert b.tiles.valid_pos == {(350, 250),
                                 (250, 350),
                                 (550, 450),
                                 (450, 550)}
    assert not b.full


def test_update():
    """Test for the update function"""
    ts = Tiles(90, 8, 8, 100)
    p = Player(ts)
    c = Computer(ts)
    b = Board(100, 8, 8, ts, p, c)

    b.update(3, 2)

    assert b.tiles.tiles_list[3][2].color == 0
    assert not b.player.stop_play
    assert not b.tiles.check_black
    assert b.tiles.tiles_list[3][3].color == 0
    assert b.tiles.valid_pos == {(250, 250),
                                 (450, 250),
                                 (250, 450)}
    assert b.tiles.black_count == 4
    assert b.tiles.white_count == 1
    assert b.tiles.count == 5

    b.update(0, 0)
    pos = {(2, 2),
           (2, 4),
           (4, 2)}
    success = False
    for (x, y) in pos:
        if ts.tiles_list[x][y] != 0:
            success = True

    assert success
    assert not b.computer.stop_play
    assert b.computer.prior == []
    assert b.computer.tiles.check_black
    assert b.computer.tiles.black_count == 3
    assert b.computer.tiles.white_count == 3
    assert b.computer.tiles.count == 6
