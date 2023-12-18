import turtle as t
import random

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

    # sets ball movement randomly
    def ball_rand_dir(self, ball):
        neg1 = random.random() > .5
        neg2 = random.random() > .5
        ball.dx = -8 if neg1 else 8
        ball.dy = -(random.random()) * 10 if neg2 else random.random() * 10

    # creates a ball at center of screen
    def create_ball(self):
        ball = t.Turtle()
        ball.shape("circle")
        ball.color("white")
        ball.up()
        ball.dx = 0
        ball.dy = 0
        self.ball_rand_dir(ball)
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
        elif (self.ball.xcor() < -240 and self.ball.xcor() > -250) and (self.ball.ycor() < self.p1.ycor() + 50 and self.ball.ycor() > self.p1.ycor() - 50):
            self.ball.setx(-240)
            self.ball.dx *= -1

    # check if ball goes off screen
    def off_screen(self):
        if self.ball.xcor() > 290:
            self.ball.setposition(0, 0)
            self.ball.dx *= -1
            self.points[0] += 1
        elif self.ball.xcor() < -290:
            self.ball.setposition(0, 0)
            self.ball.dx *= -1
            self.points[1] += 1

    # check if ball hits top or bottom
    def top_collision(self):
        if self.ball.ycor() > 250:
            self.ball.sety(250)
            self.ball.dy *= -1
        elif self.ball.ycor() < -250:
            self.ball.sety(-250)
            self.ball.dy *= -1

    # move p1 up
    def p1_up(self):
        self.p1.dy = 10

    # move p1 down
    def p1_down(self):
        self.p1.dy = -10

    # move p2 up
    def p2_up(self):
        self.p2.dy = 10

    # move p2 down
    def p2_down(self):
        self.p2.dy = -10

    # sets up game screen to play
    def play(self, screen):
        while(True):
            if self.p1.ycor() > 200:
                self.p1.sety(200)
                self.p1.dy = 0
            elif self.p1.ycor() < -200:
                self.p1.sety(-200)
                self.p1.dy = 0
            else:
                self.p1.sety(self.p1.ycor() + self.p1.dy)

            if self.p2.ycor() > 200:
                self.p2.sety(200)
                self.p2.dy = 0
            elif self.p2.ycor() < -200:
                self.p2.sety(-200)
                self.p2.dy = 0
            else:
                self.p2.sety(self.p2.ycor() + self.p2.dy)

            self.ball.setx(self.ball.xcor() + self.ball.dx)
            self.ball.sety(self.ball.ycor() + self.ball.dy)

            # end if game over
            if self.gameover():
                screen.clearscreen()
                screen.bgcolor("black")
                str = self.winner + " wins!"
                self.score.setpos(0, 0)
                self.score.write(str, align="center", font=("comic sans", 48))
                self.score.setpos(0, -75)
                self.score.write("Click to exit", align="center", font=("comic sans", 24))

                screen.exitonclick()
                return True

            # draw stuff, check not out of bounds
            self.check_collision()

            temp = [self.points[0], self.points[1]]

            self.off_screen()
            self.top_collision()

            if (temp[0] != self.points[0] or temp[1] != self.points[1]):
                self.score.clear()
                self.score.write("P1: {}      P2: {}".format(self.points[0], self.points[1]), align="center", font=("comic sans", 24))

            # Move paddles
            t.listen()
            t.onkeypress(self.p1_up, "w")
            t.onkeypress(self.p1_down, "s")
            t.onkeypress(self.p2_up, "Up")
            t.onkeypress(self.p2_down, "Down")
