import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
walker = turtle.Turtle()
walker.shape("turtle")
walker.speed(15)
walker.width(15)

# Define colors
colors = ["#8B0000", "#4682B4", "#556B2F", "#DAA520", "#6A5ACD", "#FF8C00", "#FF69B4", "#20B2AA"]

# Random walk
last_angle = 0  # Initialize to a valid angle
second_last_angle = 0  # Track the second last angle
for _ in range(250):
    walker.color(random.choice(colors))
    angle = random.choice([0, 90, 180, 270])
    while angle == (last_angle + 180) % 360 or angle == (second_last_angle + 180) % 360:  # Ensure it does not repeat back
        angle = random.choice([0, 90, 180, 270])
    walker.right(angle)
    walker.forward(30)
    second_last_angle = last_angle
    last_angle = angle

# Hide the turtle and display the result
walker.hideturtle()
turtle.done()
