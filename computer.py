import random


class Computer:
    """The computer AI"""
    def __init__(self, tiles):
        """Constructors for a computer class"""
        self.tiles = tiles
        # Use a boolean to determine the computer
        # has at least a legal move or not.
        self.stop_play = False
        # Use a list to save the positions
        # that the computer place a tile in priority
        self.prior = []
        # Use a list to save the four positions of
        # corner squares on the board
        self.corner_squares_pos = []
        self.corner_squares_pos.append(self.tiles.pos[0][0])
        self.corner_squares_pos.append(self.tiles.pos[0][7])
        self.corner_squares_pos.append(self.tiles.pos[7][0])
        self.corner_squares_pos.append(self.tiles.pos[7][7])

    def ai_put_down_tile(self):
        """Computer AI put down a tile in a correct and effective place"""
        if self.tiles.valid_pos != set():
            self.stop_play = False
            self.prior_position()
            # If the prior list isn't empty,
            # the computer will use this list to pick up a random legal move
            if self.prior != []:
                random_pos = random.choice(self.prior)
                for row in range(len(self.tiles.pos)):
                    for col in range(len(self.tiles.pos)):
                        if self.tiles.pos[row][col] == random_pos:
                            index = (row, col)
                self.tiles.add_tile(*index)
            # The computer will pick up a legal move
            # from the valid position list in random
            else:
                random_pos = random.choice(list(self.tiles.valid_pos))
                for row in range(len(self.tiles.pos)):
                    for col in range(len(self.tiles.pos)):
                        if self.tiles.pos[row][col] == random_pos:
                            index = (row, col)
                self.tiles.add_tile(*index)
            self.tiles.return_flip_pos(*index)
            self.tiles.flip_tile()
            self.tiles.return_valid_position()
            self.prior = []
        else:
            self.stop_play = True
            self.tiles.check_black = True
            self.tiles.return_valid_position()

    def prior_position(self):
        """Get the priot positions
        where AI will put down the tile in priority"""
        if self.tiles.valid_pos != set():
            for pos in self.tiles.valid_pos:
                if pos in self.corner_squares_pos:
                    self.prior.append(pos)
