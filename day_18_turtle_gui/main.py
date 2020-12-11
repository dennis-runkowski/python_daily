"""Turtle Art"""

import turtle as turtle_module
import random
import colorgram

turtle_module.colormode(255)
win = turtle_module.Screen()


def main(columns=10, dots=100):
    """Create Art"""
    t = turtle_module.Turtle()
    t.speed('fastest')
    t.penup()
    t.hideturtle()
    colors = colorgram.extract('art.jpg', 30)
    rgb_colors = []
    for color in colors:
        rgb_colors.append(
            (
                color.rgb.r,
                color.rgb.g,
                color.rgb.b
            )
        )
    rgb_colors.pop(0)
    rgb_colors.pop(0)
    rgb_colors.pop(0)

    t.setheading(225)
    t.forward(300)
    t.setheading(0)

    length = 50 * columns
    for dot_count in range(1, dots + 1):
        t.dot(20, random.choice(rgb_colors))
        t.forward(50)

        if dot_count % columns == 0:
            t.setheading(90)
            t.forward(50)
            t.setheading(180)
            t.forward(length)
            t.setheading(0)

    win.exitonclick()

if __name__ == "__main__":
    main()
