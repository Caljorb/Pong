import turtle as t

class Game:

    p1 = None
    p2 = None

    # creates a paddle with given location on screen
    def create_paddle(self, x):
        p = t.Turtle()
        p.shape("square")
        p.color("white")
        p.shapesize(stretch_wid=5, stretch_len=1)
        p.up()
        p.goto(x, 0)
        p.dy = 0 # what is dy
        return p

    def create_game_layout(self):
        self.p1 = self.create_paddle(-350)
        self.p2 = self.create_paddle(350)

    def __init__(self, screen):
        screen.clearscreen()
        screen.bgcolor("black")
        screen.title("Pong")
        self.create_game_layout()
