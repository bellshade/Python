# informasi tentang sierpinksi triangle
# https://mathigon.org/course/fractals/sierpinski

import turtle

name = "sierpinksi triangle"


points = [
    [
        -175,
        -125,
    ],
    [0, 175],
    [175, -125],
]


def get_mid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def triangle(points, depth):

    drawing.up()
    drawing.goto(points[0][0], points[0][1])
    drawing.down()
    drawing.goto(points[1][0], points[1][1])
    drawing.goto(points[2][0], points[2][1])
    drawing.goto(points[0][0], points[0][1])

    if depth > 0:
        triangle(
            [points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])],
            depth - 1,
        )
        triangle(
            [points[1], get_mid(points[0], points[1]), get_mid(points[1], points[2])],
            depth - 1,
        )
        triangle(
            [points[2], get_mid(points[2], points[1]), get_mid(points[0], points[2])],
            depth - 1,
        )


if __name__ == "__main__":

    drawing = turtle.Turtle()
    # drawing.ht()
    # drawing.speed(5)
    # drawing.pencolor("black")
    # triangle(points, 4)
