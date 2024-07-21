from turtle import Turtle, Screen
from random import choice

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.pensize(10)
colors = ["gold", "dark gray", "yellow", "deep sky blue", "pink", "blue violet"]

i = 3

while i < 10:
    timmy_the_turtle.color(choice(colors))
    for _ in range(i):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(360/i)
    i += 1

screen = Screen()
screen.exitonclick()


color_list = [(211, 210, 210), (189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (210, 212, 214), (208, 211, 208), (211, 209, 210), (64, 43, 43), (171, 183, 170), (136, 149, 69), (127, 160, 172), (101, 79, 89), (83, 133, 108), (108, 39, 44), (39, 61, 47), (45, 40, 41), (211, 196, 124), (174, 150, 152), (36, 71, 88), (179, 106, 80), (36, 67, 84), (207, 185, 181), (99, 140, 119), (184, 198, 181), (148, 116, 120), (204, 183, 186), (180, 195, 200), (53, 69, 59), (122, 129, 135)]
