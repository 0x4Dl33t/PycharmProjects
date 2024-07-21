from turtle import Turtle, Screen
from random import randrange, choice

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.pensize(5)
timmy_the_turtle.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "red", "green"]

i = 1
while i > 0:
    timmy_the_turtle.color(choice(colors))
    for _ in range(i):
        if randrange(3) == 0:
            timmy_the_turtle.left(90)
        else:
            timmy_the_turtle.right(90)
        timmy_the_turtle.forward(10)
    i += 1

screen = Screen()
screen.exitonclick()



