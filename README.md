# Othello Game

    a strategy board game for two players (Black and White)

* The game is played with black-and-white tiles on an 8x8 board. The object of the game is to have more tiles of your color than your opponent has of theirs.
* Play begins with 4 tiles in the middle, two white and two black.
* Black goes first. That player lays down a tile, which must be in a legal position. Any white tiles in between the new black tile and an existing black tile get flipped. Here’s what happens if I put a black tile above the northwest white tile -- it flips and becomes a black tile, so now I’m winning
* White and black continue to take turns until eventually the board fills up and there are no more legal moves. In the finished game below the computer has won 42 to 22

## Design and pseudocode for the Othello game_controller

1. Classes: 
- Tile : represent a single Tile
- Tiles: represent all tiles that would be put down on the board
- Board: represent the board
- GameController: detemine who wins the game and show the result
- Player: represent the behavior of the human player
- Computer: represent the behavior of the computer player

- Main processing pyde file
  - othello.pyde: run all the codes

2. functions:
- Tile class:
    - constructors: 
        x, y, color, diameter -> x, y, color, diameter
    - display:
        Draw the tile
- Tiles class:
    - constructors: 
    ```
        position, diameter, rows, columns -> pos, diameter
        black_count = 2, white_count = 2, count = 4, total_final_count
        WHITE, BLACK, tiles_list = 8*8 nested list, check_black = True
        valid_pos = set(), flip_pos = set()
        add four tiles in tiles_list:
            formula of one of the tile's position: area = len(pos)-2)/2
            for row in (area, area+2)
                for col in (area, area+2)
                    if row == col
                        Tile(black) -> tiles_list[row][col]
                    else
                        Tile(white) -> tiles_list[row][col]
    ```
    - add_tile(row, col):
    ```
        Add a tile on the correct position
        if the position in the tiles_list is 0
            if check_black is True  
                Tile(black) -> tiles_list[row][col]
                black_count++
                check_black = False
            else
                Tile(white) -> tiles_list[row][col]
                white_count++
                check_black = True
    ```
    - display: 
        draw each tile in the tiles_list unless it is 0
    - check_empty:
        check whether all the positions is filled up(if count != total_final_count)
    - valid_position:
        ```return the valid positions that could be placed a tile
        if check_black is true:
            for all 0 in tiles_list
                for all black tiles:
                    if x_blank == x_black
                        if a = |y_black - y_black| >= 1
                            for all positions between these 2 position
                                if all positions are white tiles  
                                    position -> the valid_pos
                                else
                                    continue
                    elif y_blank == y_black
                        similar to the upper code
                    elif x_blank - x_black == y_blank - y_black
                        similar to the upper code
                    elif x_blank + y_blank == x_black + x_black
                        similar to the upper code
        else
            similar to if check_black is true, but change the tile's color to white```
    - flip_position:
        return all positions that should be flipped
        ```if check_black is false:
            for all black tiles:
                flip = set()
                if x_blank == x_black
                        if a = |y_black - y_black| >= 1
                            for all positions between these 2 position
                                if all positions are white tiles
                                    position -> flip
                                    flip_set += flip
                                else
                                    break
                elif y_blank == y_black
                    similar to the upper code
                elif x_blank - x_black == y_blank - y_black
                    similar to the upper code
                elif x_blank + y_blank == x_black + x_black
                    similar to the upper code
        else
            similar to if check_black is true, but change the tile's color to white```
    - flip_tile:
        flip all the tiles that should be flipped
        ```if check_black is False
            for all positions in flip_pos
                Tile(black) -> tiles_list[row][col]```
- Board class:
    - constructors: 
        size, rows, columns, diameter -> size, rows, columns, diameter
        position = a nested list that save all the center positions of all squares on the board
        player -> player
        computer -> computer
        tiles = Tiles
        full = False
        tiles.valid_position()
    - update
        Update the board when adding tiles until all squares is filled up
        if tiles.check_black
            player.put_down_tile()
        else
            computer.ai_put_down_tile()
        if tiles.check_empty is false
            full = True
    - display
        Draw the board lines and the current tiles
- Player class:
    - constructors:
        tiles -> tiles
    - put_down_tile:
        player put down a tile
        tiles.add_tile()
        tiles.file_position()
        tiles.flip_tiles()
        tiles.valid_position()
- Computer class:
    import random
    - constructors:
        tiles -> tiles
        prior = set()   
    - ai_put_down_tile
        computer ai put down a tile in a correct and effective place
        self.prior_position()
        tiles.add_tile(random.choice(prior))
        tiles.file_position()
        tiles.flip_tiles()
        tiles.valid_position()
        self.prior = set()
    - prior_position
        return the priot positions where AI will put down the tile in priority
        if the blank position is one of the corner squares
            position -> prior
        if nothing in prior
            prior = tiles.valid_pos
- GameController class
    - constructors:
        text_position -> text_position
        board -> board
    - update:
        Detemine who is the winner and print the result when the game is over
        if board.tiles.black_count > board.tiles.white_count
            print_text: PLAYER WINS
        elif board.tiles.black_count < board.tiles.white_count
            print_text: COMPUTER WINS
        elif board.tiles.black_count == board.tiles.white_count
            print_text: TIE
        print_text: board.tiles.black_count and board.tiles.white_count
    - print_text:
        Print the text on the screen with specified fontsize and position
3.
- When the user tries to make an illegal move: nothing will happen
- When the user makes a legal move -> Player.put_down_tile()
- When its the computers turn -> Computer.ai_put_down_tile()
- When the game is over (there are no more legal moves) -> GameController.update()

  1. to end the game:
  2. no square on the list - end the game
  3. when the player and the computer have no legal moves(no valid position), set a variable to calculate the number
  no legal moves(1, 2). When it is 2, end the game.

## Computer AI Design for Othello Game

**1. Did you attempt to make your computer player very smart -- i.e., do something more clever than just pick a random legal move?**

Yes. I tried to make a prior position list for the computer AI to save the legal moves that make it play the game in a more effective way.

**2. If so, were you able to accomplish this? Is your computer player as smart as you would like?**

I have accomplished it. When it's the computer player's turn, what it acts is what I expected. 

**3. How did you determine which piece to play next? Tell us about your “pick next move” algorithm**

We know that in this game, it is important for a player to place the tiles on the corner of the board as soon as possible,
in order to have more safe tiles that wouldn't be flipped. 
Because of this, I created a list to save the position of the four corner squares of the board. When it's the turn of the computer player, 
it will get the valid position list of the white tiles. Then, every valid position in the valid position list will be checked if it is one of
the position of the four corner squares by looping the valid position list to check if it is also in the list of the four corner squares. 
If so, the position will be saved in the prior list. After the loop, the computer player will pick up a random position from the prior list
and put down the tile on this position.

**4. How often did your computer program beat you, or your friends, or whoever tested it out for you?**

My computer AI's win rate is about 13%.

**5. How would you improve it in the future?**

In the future, I want to improve the position strategy for the computer AI by extend the position list to save more possible prior positions,
and also, the possible prior list would be changed automatically when it is the computer's turn.
For example, when the computer AI have placed a tile on the top-left corner, the possible prior list will be changed - it will not only
have the four corner squares, but also includes all positions on the board edges that include the top-left corner. When placing tiles near
the corner it have occupied and also on the edges, there will be more safe tiles that wouldn't be flipped for the computer AI.

