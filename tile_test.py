from tile import Tile


def test_constructor():
    """Test for the constructor of the Tiles class"""
    t = Tile(50, 40, 10, 80)

    assert t.x == 50
    assert t.y == 40
    assert t.color == 10
    assert t.diameter == 80
