import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Square")
screen.bgcolor("white")

# Create a turtle named "square_turtle"
square_turtle = turtle.Turtle()
square_turtle.shape("turtle")
square_turtle.color("blue")

# Draw a square
for _ in range(4):
    square_turtle.forward(100)  # Move forward by 100 units
    square_turtle.right(90)     # Turn right by 90 degrees

# Hide the turtle and display the window
square_turtle.hideturtle()
turtle.done()

# Keep the window open
screen.mainloop()

