import turtle as t
import random

# ...existing code...

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(random.random(), random.random(), random.random())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)

t.speed("fastest")
draw_spirograph(5)

# ...existing code...

t.done()
