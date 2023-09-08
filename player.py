
class Player:
    """A player"""
    def __init__(self, tiles):
        """Constructors for a player class"""
        self.tiles = tiles
        # Use a boolean to determine the player
        # has at least a legal move or not.
        self.stop_play = False

    def put_down_tile(self, row, col):
        """Player put down a tile"""
        if self.tiles.valid_pos != set():
            self.stop_play = False
            self.tiles.add_tile(row, col)
            if self.tiles.place_success:
                self.tiles.return_flip_pos(row, col)
                self.tiles.flip_tile()
            self.tiles.return_valid_position()
        else:
            self.stop_play = True
            self.tiles.check_black = False
            self.tiles.return_valid_position()
