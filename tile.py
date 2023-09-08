
class Tile:
    """A tile"""
    def __init__(self, x, y, color, DIAMETER):
        """Constructors for the Tile class"""
        self.x = x
        self.y = y
        self.color = color
        self.diameter = DIAMETER

    def display(self):
        """Draw the tile"""
        STROKE_COLOR = 0
        STROKE_WEIGHT = 3

        stroke(STROKE_COLOR)
        strokeWeight(STROKE_WEIGHT)
        fill(self.color)
        ellipse(self.x, self.y, self.diameter, self.diameter)
