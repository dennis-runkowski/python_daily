"""Turtle race game"""

from turtle import Turtle, Screen
import random


def main():
    """Race Game"""
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(
        title="Make your bet",
        prompt="Which turtle will win the race? Enter a color: "
    )
    colors = [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "purple"    
    ]
    y_positions = [
        -70,
        -40,
        -10,
        20,
        50,
        80
    ]
    turtles = []
    for turtle_index in range(0, 6):
        t = Turtle(shape="turtle")
        t.penup()
        t.color(colors[turtle_index])
        t.goto(x=-230, y=y_positions[turtle_index])
        turtles.append(t)

    if user_bet:
        race_on = True
        while race_on:
            for t in turtles:
                if t.xcor() > 230:
                    winning_color = t.pencolor()
                    if winning_color == user_bet:
                        print(
                            f"You Won! The winning turtle is {winning_color}"
                        )
                    else:
                        print(
                            f"You Lost! The winning turtle is {winning_color}"
                        )
                    race_on = False

                r_distance = random.randint(0, 10)
                t.forward(r_distance)
    screen.exitonclick()
    return


if __name__ == "__main__":
    main()
