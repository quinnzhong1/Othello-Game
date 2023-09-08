from tile import Tile


class Tiles:
    """A set of tiles"""
    def __init__(self, DIAMETER, ROWS, COLUMNS, SIZE):
        """Constructors for the Tiles class"""
        self.black_count = 0
        self.white_count = 0
        self.count = 0
        self.ROWS = ROWS
        self.COLUMNS = COLUMNS
        # The number of all squares on the board
        self.TOTAL_FINAL_COUNT = ROWS * COLUMNS
        self.WHITE = 255
        self.BLACK = 0
        self.SIZE = SIZE
        self.distance = int(self.SIZE/2)
        # Create an nested list occupied by 0.
        # Use this list to save all central postions of
        # all the squares on the board
        self.pos = [[0] * self.COLUMNS for i in range(self.ROWS)]
        for row in range(self.ROWS):
            for col in range(self.COLUMNS):
                self.pos[row][col] = (col*self.SIZE + self.distance,
                                      row*self.SIZE + self.distance)
        self.DIAMETER = DIAMETER
        # Creat a nested list to save Tile classes
        self.tiles_list = [[0] * COLUMNS for i in range(ROWS)]
        # Put down the first four tiles on the center area of the board
        mid_area_position = int((len(self.pos)-2)/2)
        for row in range(mid_area_position, mid_area_position+2):
            for col in range(mid_area_position, mid_area_position+2):
                # Put down two white tiles on the correct positions
                if row == col:
                    self.tiles_list[row][col] = Tile(self.pos[row][col][0],
                                                     self.pos[row][col][1],
                                                     self.WHITE,
                                                     self.DIAMETER)
                    self.white_count += 1
                # Put down two black tiles on the correct positions
                else:
                    self.tiles_list[row][col] = Tile(self.pos[row][col][0],
                                                     self.pos[row][col][1],
                                                     self.BLACK,
                                                     self.DIAMETER)
                    self.black_count += 1
                self.count += 1
        # Use a boolean to alternate the turn between
        # the player and the computer
        # The player use the black tiles and the computer use the white tiles
        self.check_black = True
        # Use a set to save the legal moves
        self.valid_pos = set()
        # Use a set to save the tiles that should be flipped
        self.flip_pos = set()
        # Use a boolean to determine whether the tile is placed successfully
        self.place_success = True

    def add_tile(self, row, col):
        """Add a tile on the correct position"""
        # If the position is placed by a 0, it is an empty and valid position
        # to put down a tile
        if self.tiles_list[row][col] == 0:
            if self.check_black:
                # If it is the turn of the player, put down a black tile
                if self.pos[row][col] in self.valid_pos:
                    self.tiles_list[row][col] = Tile(self.pos[row][col][0],
                                                     self.pos[row][col][1],
                                                     self.BLACK,
                                                     self.DIAMETER)
                    self.black_count += 1
                    self.count += 1
                    self.check_black = False
                    self.place_success = True
                else:
                    self.place_success = False
            else:
                # If it is the turn of the computer, put down a white tile
                if self.pos[row][col] in self.valid_pos:
                    self.tiles_list[row][col] = Tile(self.pos[row][col][0],
                                                     self.pos[row][col][1],
                                                     self.WHITE,
                                                     self.DIAMETER)
                    self.white_count += 1
                    self.count += 1
                    self.check_black = True
                    self.place_success = True
                else:
                    self.place_success = False
        else:
            self.place_success = False

        # Clean the valid position set
        self.clean_val_pos()

    def display(self):
        """Draw all the exist tiles"""
        for row in self.tiles_list:
            for tile in row:
                if tile != 0:
                    # If the position is not placed by a 0,
                    # the position is occupied by a tile,
                    # and this tile shound be drawed
                    tile.display()

    def check_empty(self):
        """Check whether all the positions is filled up"""
        if self.count != self.TOTAL_FINAL_COUNT:
            return True
        else:
            return False

    def return_valid_position(self):
        """Get the valid postions for each turn"""
        if self.check_black:
            self.valid_position(self.BLACK, self.WHITE)
        else:
            self.valid_position(self.WHITE, self.BLACK)

    def valid_position(self, color_1, color_2):
        """Get the valid postions that could be placed a correct color tile"""
        # for all empty squares
        for x_blank in range(self.ROWS):
            for y_blank in range(self.COLUMNS):
                if self.tiles_list[x_blank][y_blank] == 0:
                    # for all specified-color tiles on the board
                    for x in range(self.ROWS):
                        for y in range(self.COLUMNS):
                            if (self.tiles_list[x][y] != 0
                               and self.tiles_list[x][y].color
                               == color_1):
                                # horizonal
                                if x_blank == x:
                                    gap = abs(y_blank - y)
                                    sign = int(gap/(y_blank - y))
                                    if gap > 1:
                                        # for all position between
                                        # the square and
                                        # the specified-color tile
                                        for i in range(y + sign,
                                                       y + sign*gap,
                                                       sign):
                                            if (self.tiles_list[x][i] != 0
                                               and
                                               self.tiles_list[x][i].color == color_2):
                                                if i == y + sign*(gap-1):
                                                    self.valid_pos.add(self.pos[x_blank][y_blank])
                                                    break
                                                else:
                                                    continue
                                            else:
                                                break
                                # veritical
                                elif y_blank == y:
                                    gap = abs(x_blank - x)
                                    sign = int(gap/(x_blank - x))
                                    if gap > 1:
                                        for i in range(x + sign,
                                                       x + sign*gap,
                                                       sign):
                                            if (self.tiles_list[i][y] != 0
                                               and self.tiles_list[i][y].color == color_2):
                                                if i == x + sign*(gap-1):
                                                    self.valid_pos.add(self.pos[x_blank][y_blank])
                                                    break
                                                else:
                                                    continue
                                            else:
                                                break
                                # diagonal from top left to bottom right
                                elif (x_blank - x) == (y_blank - y):
                                    gap = abs(x_blank - x)
                                    sign = int(gap/(x_blank - x))
                                    if gap > 1:
                                        for (i, j) in zip(range(x + sign, x + sign*gap, sign),
                                                          range(y + sign, y + sign*gap, sign)):
                                            if (self.tiles_list[i][j] != 0
                                               and
                                               self.tiles_list[i][j].color == color_2):
                                                if i == x + sign*(gap-1):
                                                    self.valid_pos.add((self.pos[x_blank][y_blank]))
                                                    break
                                                else:
                                                    continue
                                            else:
                                                break
                                # diagonal from top right to bottom left
                                elif (x_blank + y_blank) == (x + y):
                                    gap = abs(x_blank - x)
                                    sign_x = int(gap/(x_blank - x))
                                    sign_y = int(abs(y_blank - y)/(y_blank - y))
                                    if gap > 1:
                                        for (i, j) in zip(range(x + sign_x, x + sign_x*gap, sign_x),
                                                          range(y + sign_y, y + sign_y*gap, sign_y)):
                                            if (self.tiles_list[i][j] != 0
                                               and
                                               self.tiles_list[i][j].color == color_2):
                                                if i == x + sign_x*(gap-1):
                                                    self.valid_pos.add((self.pos[x_blank][y_blank]))
                                                    break
                                                else:
                                                    continue
                                            else:
                                                break

    def flip_position(self, color_1, color_2, row, col):
        """find all specified-color tiles' positions that need to be flipped"""
        # for all the specified-color tiles
        for x in range(self.ROWS):
            for y in range(self.COLUMNS):
                if (self.tiles_list[x][y] != 0
                   and self.tiles_list[x][y].color
                   == color_1 and ((row != x) or (col != y))):
                    # horizonal
                    if row == x:
                        gap = abs(col - y)
                        sign = int(gap/(col - y))
                        if gap > 1:
                            flp_position = set()
                            # for all position between
                            # the square and the specified-color tile
                            for i in range(y + sign, y + sign*gap, sign):
                                if (self.tiles_list[x][i] != 0
                                   and
                                   self.tiles_list[x][i].color == color_2):
                                    if i == y + sign*(gap-1):
                                        flp_position.add((x, i))
                                        self.flip_pos = self.flip_pos.union(flp_position)
                                        break
                                    else:
                                        flp_position.add((x, i))
                                        continue
                                else:
                                    break
                    # veritical
                    elif col == y:
                        gap = abs(row - x)
                        sign = int(gap/(row - x))
                        if gap > 1:
                            flp_position = set()
                            for i in range(x + sign, x + sign*gap, sign):
                                if (self.tiles_list[i][y] != 0
                                   and
                                   self.tiles_list[i][y].color == color_2):
                                    if i == x + sign*(gap-1):
                                        flp_position.add((i, y))
                                        self.flip_pos = self.flip_pos.union(flp_position)
                                        break
                                    else:
                                        flp_position.add((i, y))
                                        continue
                                else:
                                    break
                    # diagonal from top left to bottom right
                    elif (row - x) == (col - y):
                        gap = abs(row - x)
                        sign = int(gap/(row - x))
                        if gap > 1:
                            flp_position = set()
                            for (i, j) in zip(range(x + sign, x + sign*gap, sign),
                                              range(y + sign, y + sign*gap, sign)):
                                if (self.tiles_list[i][j] != 0
                                   and
                                   self.tiles_list[i][j].color == color_2):
                                    if i == x + sign*(gap-1):
                                        flp_position.add((i, j))
                                        self.flip_pos = self.flip_pos.union(flp_position)
                                        break
                                    else:
                                        flp_position.add((i, j))
                                        continue
                                else:
                                    break
                    # diagonal from top right to bottom left
                    elif (row + col) == (x + y):
                        gap = abs(row - x)
                        sign_x = int(gap/(row - x))
                        sign_y = int(abs(col - y)/(col - y))
                        if gap > 1:
                            flp_position = set()
                            for (i, j) in zip(range(x + sign_x, x + sign_x*gap, sign_x),
                                              range(y + sign_y, y + sign_y*gap, sign_y)):
                                if (self.tiles_list[i][j] != 0
                                   and
                                   self.tiles_list[i][j].color == color_2):
                                    if i == x + sign_x*(gap-1):
                                        flp_position.add((i, j))
                                        self.flip_pos = self.flip_pos.union(flp_position)
                                        break
                                    else:
                                        flp_position.add((i, j))
                                        continue
                                else:
                                    break

    def return_flip_pos(self, row, col):
        """Get the flipping postions for each turn"""
        if not self.check_black:
            self.flip_position(self.BLACK, self.WHITE, row, col)
        else:
            self.flip_position(self.WHITE, self.BLACK, row, col)

    def flip_tile(self):
        """Flip all the tiles that need to be flipped"""
        if not self.check_black:
            if self.flip_pos != set():
                for (x, y) in self.flip_pos:
                    # Change the tiles into black color
                    self.tiles_list[x][y].color = self.BLACK
                    self.black_count += 1
                    self.white_count -= 1
        else:
            if self.flip_pos != set():
                for (x, y) in self.flip_pos:
                    # Change the tiles into white color
                    self.tiles_list[x][y].color = self.WHITE
                    self.white_count += 1
                    self.black_count -= 1

        # Clean the flip position set
        self.clean_flip_pos()

    def clean_val_pos(self):
        """Clean the set of valid positions"""
        self.valid_pos = set()

    def clean_flip_pos(self):
        """Clean the set of flipping positions"""
        self.flip_pos = set()
