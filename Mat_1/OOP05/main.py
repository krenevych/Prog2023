from Triangle import Triangle
from Quadrik import Quadrik
from random import randint
from turtle import *

def createFigures(number):
    # генерація випадкового числа з проміжку  [0, 10]
    colors = [
        "green yellow",
        "teal",
        "deep pink",
        "rosy brown",
        "red",
        "green",
        "black",
    ]

    bound = 350
    triangles = []
    for i in range(number):

        x1 = randint(-bound, bound)
        y1 = randint(-bound, bound)
        x2 = randint(-bound, bound)
        y2 = randint(-bound, bound)
        x3 = randint(-bound, bound)
        y3 = randint(-bound, bound)
        type = randint(0, 1)
        if type == 0:
            t = Quadrik(x1, y1, x2, y2, x3, y3)
        else:
            t = Triangle(x1, y1, x2, y2)

        color_num = randint(0, len(colors) - 1)
        t.set_color(colors[color_num])
        triangles.append(t)
    return triangles


if __name__ == '__main__':
    figures = createFigures(10)
    for t in figures:
        bound = 100
        x0 = randint(-bound, bound)
        y0 = randint(-bound, bound)
        t.set_position(x0, y0)
        t.draw()

    mainloop()