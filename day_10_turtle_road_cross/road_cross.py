import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Turtle Road Crossing Game")
screen.bgcolor("white")
screen.setup(width=1000, height=600)
screen.tracer(0)

# Score setup
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("black")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(-280, 260)
score_pen.write(f"Score: {score}", align="left", font=("Arial", 16, "normal"))

# Player turtle setup
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.goto(0, -280)
player.setheading(90)

# Function to move the player up
def move_up():
    player.forward(20)

# Keyboard binding
screen.listen()
screen.onkey(move_up, "Up")

# Car setup
cars = []
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
start_x = 500
start_y = -240

for _ in range(15):
    car = turtle.Turtle()
    car.shape("square")
    car.shapesize(stretch_wid=1, stretch_len=2)
    car.color(random.choice(colors))
    car.penup()
    car.goto(start_x, start_y)
    car.speed = random.randint(1, 2)  # Slower random speed for each car
    cars.append(car)
    start_y += 40

# Function to reset the game
def reset_game():
    global score, game_over
    score = 0
    score_pen.clear()
    score_pen.write(f"Score: {score}", align="left", font=("Arial", 16, "normal"))
    player.goto(0, -280)
    game_over = False

# Game loop
game_over = False

while True:
    screen.update()
    
    if not game_over:
        # Move cars
        for car in cars:
            car.backward(car.speed)
            if car.xcor() < -300:
                car.goto(300, car.ycor())
                car.speed = random.randint(1, 3)  # Reset speed for each car
            
            # Collision detection
            if player.distance(car) < 20:
                game_over = True
                player.color("red")
                screen.update()
                screen.ontimer(reset_game, 2000)  # Restart game after 2 seconds
    
    # Check if player has reached the top
    if player.ycor() > 280:
        player.goto(0, -280)
        score += 1
        score_pen.clear()
        score_pen.write(f"Score: {score}", align="left", font=("Arial", 16, "normal"))

# Exit on click
screen.exitonclick()
