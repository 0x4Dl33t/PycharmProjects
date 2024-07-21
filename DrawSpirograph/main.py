import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pensize(1)
        tim.speed("fastest")
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(10)
screen = Screen()
screen.exitonclick()



