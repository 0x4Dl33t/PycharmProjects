from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "indigo"]

screen = Screen()
screen.setup(width=500, height=400)
choice = screen.textinput(title="Make your bet", prompt="Bet on a turtle that will win the race. "
                                                        "\nRed, Orange, Yellow, Green, Blue or Indigo?").lower()

y_axis = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_race_on = False

for turtles in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtles])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis[turtles])
    all_turtles.append(new_turtle)

if choice:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            win_color = turtle.pencolor()
            if win_color == choice:
                is_race_on = False
                print(f"Your '{choice}' turtle has won! ")
            else:
                is_race_on = False
                print(f"Your '{choice}' turtle has lost. The winner is '{win_color}' turtle! ")
        rand_distance = random.randint(0, 30)
        turtle.forward(rand_distance)

screen.exitonclick()