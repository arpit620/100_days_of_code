# turtle
import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Hirst Painting")
screen.colormode(255)  # Enable rgb for full color range

# Hirst painting config
dots_distance = 50
rows = 10
cols = 10

# Function to generate random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)  # Return a tuple

# Turtle setup for drawing dots
artist = turtle.Turtle()
artist.speed("fastest")
artist.penup()
artist.hideturtle()

# Turtle setup for drawing path
path_drawer = turtle.Turtle()
path_drawer.speed("fastest")
path_drawer.pendown()
path_drawer.color("black")
path_drawer.hideturtle()

# Calculate starting position to center the grid
start_x = -(cols * dots_distance / 2) + (dots_distance / 2)
start_y = (rows * dots_distance / 2) - (dots_distance / 2)

# Move to initial position
artist.goto(start_x, start_y)
path_drawer.goto(start_x, start_y)

# Drawing the dots and path
for row in range(rows):
    for col in range(cols):
        artist.dot(20, random_color())  # Pass the tuple directly
        path_drawer.forward(dots_distance)
        artist.forward(dots_distance)
    artist.setx(start_x)
    # artist.left(90)
    artist.backward(dots_distance * cols)
    artist.right(90)
    artist.forward(dots_distance)  # Move down by dots_distance
    artist.left(90)
    
    path_drawer.setx(start_x)
    path_drawer.backward(dots_distance * cols)
    path_drawer.right(90)
    path_drawer.forward(dots_distance)  # Move down by dots_distance
    path_drawer.left(90)

turtle.done()
