import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Drawing with Keyboard")

# Create a turtle object
pen = turtle.Turtle()

# Define functions to move the turtle
def move_forward():
    pen.forward(10)

def move_backward():
    pen.backward(10)

def turn_left():
    pen.left(10)

def turn_right():
    pen.right(10)

def clear_screen():
    pen.clear()

# Bind keyboard keys to functions
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear_screen, "c")

# Listen for key presses
screen.listen()

# Keep the window open
screen.mainloop()
