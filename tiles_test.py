from tiles import Tiles


def test_constructor():
    """Test for the constructor of the Tiles class"""
    ts = Tiles(90, 4, 4, 100)

    assert ts.black_count == 2
    assert ts.white_count == 2
    assert ts.count == 4
    assert ts.ROWS == 4
    assert ts.COLUMNS == 4
    assert ts.TOTAL_FINAL_COUNT == 16
    assert ts.WHITE == 255
    assert ts.BLACK == 0
    assert ts.SIZE == 100
    assert ts.distance == 50
    assert ts.pos == [[(50, 50), (150, 50), (250, 50), (350, 50)],
                      [(50, 150), (150, 150), (250, 150), (350, 150)],
                      [(50, 250), (150, 250), (250, 250), (350, 250)],
                      [(50, 350), (150, 350), (250, 350), (350, 350)]]
    assert ts.DIAMETER == 90

    assert ts.tiles_list[1][1].color == 255
    assert ts.tiles_list[1][2].color == 0
    assert ts.tiles_list[2][1].color == 0
    assert ts.tiles_list[2][2].color == 255
    for i in range(4):
        assert ts.tiles_list[0][i] == 0
    for i in range(4):
        assert ts.tiles_list[3][i] == 0
    for i in range(0, 4, 3):
        assert ts.tiles_list[1][i] == 0
    for i in range(0, 4, 3):
        assert ts.tiles_list[2][i] == 0

    assert ts.check_black
    assert ts.valid_pos == set()
    assert ts.flip_pos == set()
    assert ts.place_success


def test_add_tile():
    """Test for the add_tile function"""
    ts = Tiles(90, 8, 8, 100)
    ts.return_valid_position()

    ts.add_tile(0, 0)
    assert ts.tiles_list[0][0] == 0
    assert not ts.place_success

    ts.return_valid_position()
    ts.add_tile(3, 2)
    assert ts.tiles_list[3][2].color == 0
    assert ts.place_success
    assert ts.black_count == 3
    assert ts.white_count == 2
    assert ts.count == 5
    assert not ts.check_black

    ts.return_flip_pos(3, 2)
    ts.flip_tile()
    ts.return_valid_position()

    ts.add_tile(2, 2)
    assert ts.tiles_list[2][2].color == 255
    assert ts.place_success
    assert ts.black_count == 4
    assert ts.white_count == 2
    assert ts.count == 6
    assert ts.check_black


def test_check_empty():
    """Test for the check_empty function"""
    ts = Tiles(90, 8, 8, 100)

    assert ts.check_empty()
    ts.count = 64
    assert not ts.check_empty()


def test_return_valid_position():
    """Test for the return_valid_position function"""
    ts = Tiles(90, 8, 8, 100)
    ts.return_valid_position()

    assert ts.valid_pos == {(350, 250),
                            (250, 350),
                            (550, 450),
                            (450, 550)}

    ts.add_tile(3, 2)
    ts.return_flip_pos(3, 2)
    ts.flip_tile()
    ts.return_valid_position()

    assert ts.valid_pos == {(250, 250),
                            (450, 250),
                            (250, 450)}


def test_valid_position():
    """Test for the valid_position function"""
    ts = Tiles(90, 8, 8, 100)

    ts.valid_position(0, 255)
    assert ts.valid_pos == {(350, 250),
                            (250, 350),
                            (550, 450),
                            (450, 550)}

    ts.add_tile(3, 2)
    ts.return_flip_pos(3, 2)
    ts.flip_tile()
    ts.valid_position(255, 0)
    assert ts.valid_pos == {(250, 250),
                            (450, 250),
                            (250, 450)}


def test_flip_position():
    """Test for the flip_position function"""
    ts = Tiles(90, 8, 8, 100)

    ts.return_valid_position()
    ts.add_tile(3, 2)
    ts.flip_position(0, 255, 3, 2)
    assert ts.flip_pos == {(3, 3)}

    ts.flip_tile()
    ts.return_valid_position()
    ts.add_tile(2, 2)
    ts.flip_position(255, 0, 2, 2)
    assert ts.flip_pos == {(3, 3)}


def test_return_flip_pos():
    """Test for the return_flip_pos function"""
    ts = Tiles(90, 8, 8, 100)

    ts.return_valid_position()
    ts.add_tile(3, 2)
    ts.return_flip_pos(3, 2)
    assert ts.flip_pos == {(3, 3)}

    ts.flip_tile()
    ts.return_valid_position()
    ts.add_tile(2, 2)
    ts.return_flip_pos(2, 2)
    assert ts.flip_pos == {(3, 3)}


def test_flip_tile():
    """Test for the flip_tile function"""
    ts = Tiles(90, 8, 8, 100)

    ts.return_valid_position()
    ts.add_tile(3, 2)
    ts.return_flip_pos(3, 2)
    ts.flip_tile()
    assert ts.tiles_list[3][3].color == 0

    ts.return_valid_position()
    ts.add_tile(2, 2)
    ts.return_flip_pos(2, 2)
    ts.flip_tile()
    assert ts.tiles_list[3][3].color == 255


def test_clean_val_pos():
    """Test for the clean_val_pos function"""
    ts = Tiles(90, 8, 8, 100)

    ts.clean_val_pos()
    assert ts.valid_pos == set()


def test_clean_flip_pos():
    """Test for the clean_flip_pos function"""
    ts = Tiles(90, 8, 8, 100)

    ts.return_valid_position()
    ts.add_tile(3, 2)
    ts.return_flip_pos(3, 2)
    ts.clean_flip_pos()
    assert ts.flip_pos == set()
