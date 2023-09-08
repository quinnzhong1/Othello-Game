from player import Player
from tiles import Tiles


def test_constructor():
    """Test for the constructor of the Player class"""
    ts = Tiles(90, 4, 4, 100)
    p = Player(ts)

    assert p.tiles == ts
    assert not p.stop_play


def test_put_down_tile():
    """Test for the put_down_tile function"""
    ts = Tiles(90, 8, 8, 100)
    p = Player(ts)
    p.tiles.return_valid_position()

    p.put_down_tile(3, 2)

    assert not p.stop_play
    assert p.tiles.tiles_list[3][2].color == 0
    assert not p.tiles.check_black
    assert p.tiles.tiles_list[3][3].color == 0
    assert p.tiles.valid_pos == {(250, 250),
                                 (450, 250),
                                 (250, 450)}
    assert p.tiles.black_count == 4
    assert p.tiles.white_count == 1
    assert p.tiles.count == 5
