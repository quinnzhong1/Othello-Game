

class Board:
    """A chess board"""
    def __init__(self, SIZE, ROWS, COLUMNS, tiles, player, computer):
        """Constructors for the Board class"""
        self.SIZE = SIZE   # The square size
        self.ROWS = ROWS
        self.COLUMNS = COLUMNS
        self.player = player
        self.computer = computer
        self.tiles = tiles
        # Get the initial valid positions for the player
        self.tiles.return_valid_position()
        # Use self.full to detemine whether the board is filled up
        self.full = False

    def update(self, row, column):
        """Update the board when adding tiles until all squares is filled up"""
        if self.tiles.check_black:
            self.player.put_down_tile(row, column)
        else:
            self.computer.ai_put_down_tile()

        if not self.tiles.check_empty():
            # If all the squares is not empty, the board is filled up
            self.full = True

    def display(self):
        """Draw the board lines and the current tiles"""
        STROKE_COLOR = 0
        STROKE_WEIGHT = 3

        stroke(STROKE_COLOR)
        strokeWeight(STROKE_WEIGHT)

        # Draw black lines for the board
        for x in range(self.SIZE, self.SIZE*(self.COLUMNS-1) + 1, self.SIZE):
            line(x, 0, x, self.SIZE*self.ROWS)

        for y in range(self.SIZE, self.SIZE*(self.ROWS-1) + 1, self.SIZE):
            line(0, y, self.SIZE*self.COLUMNS, y)

        # Draw all the tiles that was placed
        self.tiles.display()
