import turtle as t

SPOS = (105, 170)
QPOS = (-150, -150)

# Create screen
screen = t.Screen()

# W = 600, H = 500, open in top left corner
screen.setup(600, 500, 0, 0)
screen.bgcolor("black")
screen.title(":3")

# Available shapes:
# ['arrow', 'blank', 'circle', 'classic', 'square', 'triangle', 'turtle']
# adds gif to list of shapes
screen.addshape("./res/colon-three-kitty.gif")

# display on screen
cat = t.Turtle()
cat.shape("./res/colon-three-kitty.gif")

# move turtle for start
start = t.Turtle()
start.hideturtle() # arrow isn't visible
start.up() # don't draw while moving
start.left(90)
start.forward(screen.window_height() / 2 - 100)
start.right(90)
start.forward(screen.window_width() / 4)
#sPos = start.pos()
#print(sPos)

# write start
start.color("pink")
f = ('comic sans', 25)
start.write("Start", font=f, align="Center")

# move turtle for quit
quit = t.Turtle()
quit.hideturtle()
quit.up()
quit.right(90)
quit.forward(screen.window_height() / 2 - 100)
quit.right(90)
quit.forward(screen.window_width() / 4)
#qPos = quit.pos()
#print(qPos)

# write quit
quit.color("red")
quit.write("Quit", font=f, align="Center")

# make arrow indicator for selection
arrow = t.Turtle()
arrow.up()
arrow.setposition(SPOS)

# Close screen
screen.exitonclick()
