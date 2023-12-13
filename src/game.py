import turtle as t

class Game:

    p1 = None
    p2 = None
    ball = None
    score = None

    # creates a paddle with given location on screen
    def create_paddle(self, x):
        p = t.Turtle()
        p.shape("square")
        p.color("white")
        p.shapesize(stretch_wid=5, stretch_len=1)
        p.up()
        p.setposition(x, 0)
        p.dy = 0 # what is dy
        return p

    # creates a ball at center of screen
    def create_ball(self):
        ball = t.Turtle()
        ball.shape("circle")
        ball.color("white")
        return ball

    # writes scoreboard to screen
    def create_scoreboard(self):
        score = t.Turtle()
        score.color("white")
        score.up()
        score.hideturtle()
        score.setposition(0, 200)
        score.write("P1: 0      P2: 0", align="center", font=("comic sans", 24))
        return score

    # puts all elements in starting positions
    def create_game_layout(self):
        self.p1 = self.create_paddle(-250)
        self.p2 = self.create_paddle(250)
        self.ball = self.create_ball()
        self.score = self.create_scoreboard()

    # initializes game
    def __init__(self, screen):
        screen.clearscreen()
        screen.bgcolor("black")
        screen.title("Pong")
        self.create_game_layout()
