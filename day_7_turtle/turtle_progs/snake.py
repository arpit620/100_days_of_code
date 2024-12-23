import turtle
import time
import random

class Snake:
    def __init__(self):
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("black")
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "stop"
        self.segments = []

    def go_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def go_down(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def go_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def go_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"

    def move(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + 20)

        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 20)

        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 20)

        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 20)

    def add_segment(self):
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        self.segments.append(new_segment)

    def reset(self):
        self.head.goto(0, 0)
        self.head.direction = "stop"
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()

class Food:
    def __init__(self):
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("circle")
        self.food.color("red")
        self.food.penup()
        self.move_food()

    def move_food(self):
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        self.food.goto(x, y)

class Game:
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.title("Snake Game by @TokyoEdTech")
        self.wn.bgcolor("green")
        self.wn.setup(width=600, height=600)
        self.wn.tracer(0)  # Turns off the screen updates

        self.snake = Snake()
        self.food = Food()
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

        self.wn.listen()
        self.wn.onkeypress(self.snake.go_up, "Up")
        self.wn.onkeypress(self.snake.go_down, "Down")
        self.wn.onkeypress(self.snake.go_left, "Left")
        self.wn.onkeypress(self.snake.go_right, "Right")

        self.score = 0
        self.high_score = 0
        self.delay = 0.1

    def run(self):
        while True:
            self.wn.update()

            # Check for a collision with the border
            if self.snake.head.xcor() > 290 or self.snake.head.xcor() < -290 or self.snake.head.ycor() > 290 or self.snake.head.ycor() < -290:
                time.sleep(1)
                self.snake.reset()
                self.score = 0
                self.delay = 0.1
                self.update_score()

            # Check for a collision with the food
            if self.snake.head.distance(self.food.food) < 20:
                self.food.move_food()
                self.snake.add_segment()
                self.delay -= 0.001
                self.score += 10
                if self.score > self.high_score:
                    self.high_score = self.score
                self.update_score()

            # Move the end segments first in reverse order
            for index in range(len(self.snake.segments) - 1, 0, -1):
                x = self.snake.segments[index - 1].xcor()
                y = self.snake.segments[index - 1].ycor()
                self.snake.segments[index].goto(x, y)

            # Move segment 0 to where the head is
            if len(self.snake.segments) > 0:
                x = self.snake.head.xcor()
                y = self.snake.head.ycor()
                self.snake.segments[0].goto(x, y)

            self.snake.move()

            # Check for head collision with the body segments
            for segment in self.snake.segments:
                if segment.distance(self.snake.head) < 20:
                    time.sleep(1)
                    self.snake.reset()
                    self.score = 0
                    self.delay = 0.1
                    self.update_score()

            time.sleep(self.delay)

    def update_score(self):
        self.pen.clear()
        self.pen.write("Score: {}  High Score: {}".format(self.score, self.high_score), align="center", font=("Courier", 24, "normal"))

if __name__ == "__main__":
    game = Game()
    game.run()
