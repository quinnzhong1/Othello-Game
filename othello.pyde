from tiles import Tiles
from board import Board
from player import Player
from computer import Computer
from game_controller import GameController


SIZE = 100   # The square size
ROWS = 8
COLUMNS = 8
DIAMETER = 90
BACKGROUND_COLOR = (10, 105, 50)
TERMINAL_SIZE = 30
# The time delay is about 1 second
DELAY_TIME = 60
# The time delay counter
counter = 0
# Let the input function run just one time at the game beginning
begin_input = True
# Let the return_scores function run just one time at the end
begin_return_score = True
# The name that return to the scores file
name = ''

ts = Tiles(DIAMETER, ROWS, COLUMNS, SIZE)
ply = Player(ts)
cpt = Computer(ts)
b = Board(SIZE, ROWS, COLUMNS, ts, ply, cpt)
gc = GameController(SIZE*ROWS/2, b, ply, cpt)


def setup():
    # Draw the green background for the board
    background(*BACKGROUND_COLOR)
    size(SIZE*ROWS, SIZE*COLUMNS + TERMINAL_SIZE)


def draw():
    global b, gc, counter, begin_input, name, begin_return_score
    b.display()
    gc.update()

    if ts.check_black:
        gc.print_turn()

    if not ts.check_black:
        # Use a counter to execute time delay when it's the computer's turn
        if counter < DELAY_TIME:
            gc.print_turn()
            counter += 1
        else:
            b.update(0, 0)
            counter = 0

    # Enter the player's name at the beginning
    if begin_input:
        begin_input = False
        name = input('Enter your name')
    # Update the player's name and score in the scores.txt
    if gc.game_end and begin_return_score:
        begin_return_score = False
        gc.update_scores(name)


def mouseClicked():
    # Return the index to the board to add the tile in the correct position
    # Update the board and tiles
    global b
    row = mouseY // SIZE
    column = mouseX // SIZE
    if ts.check_black:
        b.update(row, column)


def input(message=''):
    # Input function
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
