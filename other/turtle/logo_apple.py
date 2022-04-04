import turtle as t


def gambar():
    t.begin_fill()
    t.fillcolor("black")
    t.left(134)
    for i in range(30):
        t.forward(1)
        t.left(1)
    t.right(5)
    for i in range(35):
        t.forward(1)
        t.left(1)
    t.left(5)
    t.forward(30)

    for i in range(15):
        t.forward(0.7)
        t.right(3)

    t.forward(25)
    t.left(5)
    for i in range(50):
        t.forward(1)
        t.left(1)
    t.right(3)
    for i in range(50):
        t.forward(1)
        t.left(1)
    t.right(5)
    for i in range(45):
        t.forward(2)
        t.left(1)
    t.right(5)
    for i in range(40):
        t.forward(2)
        t.left(1)
    t.left(5)
    for i in range(20):
        t.forward(1)
        t.left(2)
    t.left(5)
    t.forward(15)
    for i in range(9):
        t.forward(2)
        t.right(3)
    t.forward(1)
    for i in range(15):
        t.forward(1)
        t.right(1)
    t.right(4)
    t.forward(4.5)
    t.right(1)
    for i in range(27):
        t.forward(1)
        t.left(2)
    t.left(8)
    t.forward(5)
    for i in range(25):
        t.forward(2)
        t.left(1)
    t.right(3)
    t.forward(10)
    t.left(83)
    for i in range(75):
        t.forward(1.3)
        t.right(1)
    t.right(4)
    for i in range(24):
        t.forward(1.3)
        t.right(1)
    t.forward(9.66)
    t.end_fill()
    t.penup()
    t.left(132)
    t.forward(100)
    t.right(96)
    t.pendown()
    t.begin_fill()
    t.fillcolor("black")
    for i in range(60):
        t.forward(0.8)
        t.right(1)
    t.right(120)
    for i in range(60):
        t.forward(0.8)
        t.right(1)
    t.hideturtle()
    t.end_fill()
    t.done()


if __name__ == "__main__":
    gambar()
