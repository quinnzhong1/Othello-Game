from computer import Computer
from player import Player
from tiles import Tiles


def test_constructor():
    """Test for the constructor of the computer class"""
    ts = Tiles(90, 8, 8, 100)
    c = Computer(ts)

    assert c.tiles == ts
    assert not c.stop_play
    assert c.prior == []
    assert c.corner_squares_pos == [(50, 50),
                                    (750, 50),
                                    (50, 750),
                                    (750, 750)]


def test_ai_put_down_tile():
    """Test for the ai_put_down_tile function"""
    ts = Tiles(90, 8, 8, 100)
    p = Player(ts)
    c = Computer(ts)
    ts.return_valid_position()
    p.put_down_tile(3, 2)

    c.ai_put_down_tile()
    pos = {(2, 2),
           (2, 4),
           (4, 2)}
    success = False
    for (x, y) in pos:
        if ts.tiles_list[x][y] != 0:
            success = True

    assert success
    assert not c.stop_play
    assert c.prior == []
    assert c.tiles.check_black
    assert c.tiles.black_count == 3
    assert c.tiles.white_count == 3
    assert c.tiles.count == 6


def test_prior_position():
    """Test for the prior_position function"""
    ts = Tiles(90, 8, 8, 100)
    p = Player(ts)
    c = Computer(ts)
    c.tiles.return_valid_position()
    p.put_down_tile(3, 2)

    c.prior_position()

    assert c.prior == []
