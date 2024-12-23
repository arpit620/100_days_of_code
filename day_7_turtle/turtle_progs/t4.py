import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Racing Game")
screen.bgcolor("white")
screen.setup(width=800, height=600)

# Create a list of colors
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

# Ask the user to select a color for their turtle
user_color = screen.textinput("Choose Your Turtle", "Enter a color (red, blue, green, yellow, purple, orange): ").lower()

# Check if the user's color is valid
if user_color not in colors:
    screen.bye()
    raise ValueError("Invalid color selected. Please choose from the given options.")

# Create turtles
turtles = []
start_x = -380
start_y = -150

for i in range(6):
    t = turtle.Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(start_x, start_y + i * 50)
    turtles.append(t)

# Race logic
race_on = True
while race_on:
    for t in turtles:
        t.forward(random.randint(1, 10))
        if t.xcor() > 380:
            race_on = False
            winner_color = t.color()[0]
            if winner_color == user_color:
                screen.title(f"You won! The {winner_color} turtle is the winner!")
            else:
                screen.title(f"You lost! The {winner_color} turtle is the winner!")

# Keep the window open
screen.mainloop()
