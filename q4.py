import turtle as exturtle
from math import cos, sin, pi

def star(turtle, x, y, points, R, r):
    turtle.penup()
    angle = pi / 2
    first_point_x = x + r * cos(angle - 0.5 * ((2 * pi) / points))
    first_point_y = y + r * sin(angle - 0.5 * ((2 * pi) / points))

    for p in range(points):
        x1 = x + r * cos(angle + (p - 0.5) * ((2 * pi) / points))
        y1 = y + r * sin(angle + (p - 0.5) * ((2 * pi) / points))

        x2 = x + R * cos(angle + p * ((2 * pi) / points))
        y2 = y + R * sin(angle + p * ((2 * pi) / points))

        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.goto(x2, y2)

    turtle.goto(first_point_x, first_point_y)

def ring(turtle, cx, cy, Nstars, radius, points, R, r):
    turtle.bgcolor("blue")
    for n in range(Nstars):
        star_x = cx + radius * cos(n * ((2 * pi) / Nstars))
        star_y = cy + radius * sin(n * ((2 * pi) / Nstars))

        turtle.color("gold")
        turtle.begin_fill()
        star(turtle, star_x, star_y, points, R, r)
        turtle.end_fill()

"""star(exturtle, -300, 0, 5, 50, 20)
star(exturtle, -100, 0, 6, 50, 20)
star(exturtle, 100, 0, 7, 50, 20)
star(exturtle, 300, 0, 8, 50, 20)
exturtle.exitonclick()"""

ring(exturtle, 0, 0, 12, 250, 5, 40, 15)
exturtle.exitonclick()