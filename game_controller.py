import re


class GameController:
    """The Othello game controller"""
    def __init__(self, TEXT_POS, board, player, computer):
        """Constructors for the GameController class"""
        # Use TEXT_POS to detemine the position of the text
        self.TEXT_POS = TEXT_POS
        self.board = board
        self.player = player
        self.computer = computer
        self.FONTCOLOR = (255, 0, 0)
        self.game_end = False

    def update(self):
        """
        Detemine who is the winner and print the result when the game is over
        """
        # When the board is filled up(board.full is true),
        # or no one have any legal move, the game is over.
        if ((self.board.full)
           or (self.player.stop_play and self.computer.stop_play)):
            self.game_end = True

            # Print who wins
            if self.board.tiles.black_count > self.board.tiles.white_count:
                self.print_text("PLAYER WINS", -150, 0, 50)
            elif self.board.tiles.black_count < self.board.tiles.white_count:
                self.print_text("COMPUTER WINS", -190, 0, 50)
            elif self.board.tiles.black_count == self.board.tiles.white_count:
                self.print_text("TIE", -30, 0, 50)

            # Print the number of tiles
            s = "Player: " + str(self.board.tiles.black_count) + " Computer: "
            s = s + str(self.board.tiles.white_count)           
            self.print_text(s, -160, 50, 30)

    def print_text(self, string, x_offset, y_offset, fontsize):
        """Print the text on the screen with specified fontsize and position"""
        fill(*self.FONTCOLOR)
        textSize(fontsize)
        # Use offset to adjust the position of the text
        text(string, self.TEXT_POS + x_offset, self.TEXT_POS + y_offset)

    def print_turn(self):
        """Print whose turn is it now on the bottom"""
        TERMINAL_COLOR = (10, 105, 50)
        TERMINAL_SIZE = 30
        TEXT_SIZE = 20
        LENGTH = self.board.SIZE * self.board.ROWS

        if self.game_end:
            # No word in the bottom when game over
            fill(*TERMINAL_COLOR)
            rect(0, LENGTH, LENGTH, TERMINAL_SIZE)
        else:
            fill(*TERMINAL_COLOR)
            rect(0, LENGTH, LENGTH, TERMINAL_SIZE)
            fill(225)
            textSize(TEXT_SIZE)
            if self.board.tiles.check_black:
                text("It's your turn!", TEXT_SIZE, LENGTH + 22)
            else:
                text("It's computer's turn!", TEXT_SIZE, LENGTH + 22)

    def update_scores(self, name):
        """Update playes' scores to the scores.txt"""
        f_read = open('scores.txt', 'r')

        score = self.board.tiles.black_count
        message = name + ' ' + str(score)
        pattern = r'\d+'

        line = f_read.readline()
        f_read.seek(0)
        content = f_read.read()

        if line == '':
            f_write = open('scores.txt', 'w')
            f_write.write(message)
        else:
            s = re.findall(pattern, line)
            if int(s[0]) >= score:
                f_write = open('scores.txt', 'w')
                message = content + '\n' + message
                f_write.write(message)
            else:
                f_write = open('scores.txt', 'w')
                message = message + '\n' + content
                f_write.write(message)

        f_write.close()
        f_read.close()
