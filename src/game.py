import turtle as t

class Game:

    p1 = None
    p2 = None
    ball = None
    score = None

    winner = None
    points = [0, 0]

    # creates a paddle with given location on screen
    def create_paddle(self, x):
        p = t.Turtle()
        p.shape("square")
        p.color("white")
        p.shapesize(stretch_wid=5, stretch_len=1)
        p.up()
        p.setposition(x, 0)
        p.dy = 0 # change in y
        return p

    # creates a ball at center of screen
    def create_ball(self):
        ball = t.Turtle()
        ball.shape("circle")
        ball.color("white")
        ball.dx = 0
        ball.dy = 0
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

    # check if game over
    def gameover(self):
        if self.points[0] == 3:
            self.winner = "P1"
            return True
        elif self.points[1] == 3:
            self.winner = "P2"
            return True
        return False

    # check if ball hits paddle
    def check_collision(self):
        if (self.ball.xcor() > 240 and self.ball.xcor() < 250) and (self.ball.ycor() < self.p2.ycor() + 50 and self.ball.ycor() > self.p2.ycor() - 50):
            self.ball.setx(240)
            self.ball.dx *= -1
        elif (self.ball.xcor() > -240 and self.ball.xcor() < -250) and (self.ball.ycor() < self.p2.ycor() + 50 and self.ball.ycor() > self.p2.ycor() - 50):
            self.ball.setx(-240)
            self.ball.dx *= -1

    # check if ball goes off screen
    def off_screen(self):
        if self.ball.xcor() > 290:
            self.ball.setposition(0, 0)
            self.ball.dx *= -1
            self.points[0] += 1
        elif self.ball.xcor() > -290:
            self.ball.setposition(0, 0)
            self.ball.dx *= -1
            self.points[1] += 1

    # check if ball hits top or bottom
    def top_collision(self):
        if self.ball.ycor() > 490:
            self.ball.sety(490)
            self.ball.dy *= -1
        elif self.ball.ycor() < -490:
            self.ball.sety(-490)
            self.ball.dy *= -1

    def play(self):
        self.p1.sety(self.p1.ycor() + self.p1.dy)
        self.p2.sety(self.p2.ycor() + self.p2.dy)
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

        # end if game over
        if self.gameover():
            print(self.winner, " :3")

        self.check_collision()
        self.off_screen()
        self.top_collision()
        self.score.clear()
        self.score.write("P1: {}      P2: {}".format(self.points[0], self.points[1]), align="center", font=("comic sans", 24))
