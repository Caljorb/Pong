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
t.shape("./res/colon-three-kitty.gif")

# Close screen
screen.exitonclick()
