import turtle as t

# Create screen
screen = t.Screen()

# W = 600, H = 500, open in top left corner
screen.setup(600, 500, 0, 0)
screen.bgcolor("black")

# Available shapes:
# ['arrow', 'blank', 'circle', 'classic', 'square', 'triangle', 'turtle']
# adds gif to list of shapes
screen.addshape("./res/colon-three-kitty.gif")

# display on screen
cat = t.Turtle()
cat.shape("./res/colon-three-kitty.gif")

# move turtle
start = t.Turtle()
start.hideturtle() # arrow isn't visible
start.up() # don't draw while moving
start.left(90)
start.forward(screen.window_height() / 2 - 100)
start.right(90)
start.forward(screen.window_width() / 4)

# write start
f = ('comic sans', 25)
start.write("Start", font=f, align="Center")




# Close screen
screen.exitonclick()
