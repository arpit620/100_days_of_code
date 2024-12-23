import turtle
import random

# Screen setup
win = turtle.Screen()
win.title("Pong by Arpit")
win.bgcolor("black")
win.setup(width=1000, height=600)  # Increased width to 1000
win.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-450, 0)

# Paddle B (Computer)
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(450, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = -0.8  # Slower ball
ball.dy = -0.8

# Center Line
center_line = turtle.Turtle()
center_line.speed(0)
center_line.color("white")
center_line.penup()
center_line.goto(0, 300)
center_line.pendown()
center_line.setheading(270)
center_line.forward(600)

# Score
score_a = 0
score_b = 0

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function to move paddles
def paddle_a_up():
    if paddle_a.ycor() < 240:
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    if paddle_a.ycor() > -240:
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

# Computer paddle movement
def computer_paddle_move():
    y = paddle_b.ycor()
    if ball.ycor() > y:
        y += 8  # Speed of computer paddle
    else:
        y -= 8
    paddle_b.sety(y)

# Keyboard bindings
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")

# Main game loop
while True:
    win.update()
    computer_paddle_move()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        score_display.clear()
        score_display.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score_display.clear()
        score_display.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Collision with paddles
    if (ball.xcor() > 440 and ball.xcor() < 450) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(440)
        ball.dx *= -1

    if (ball.xcor() < -440 and ball.xcor() > -450) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-440)
        ball.dx *= -1
