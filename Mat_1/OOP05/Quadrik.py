from turtle import *
from random import randint
from Figure import Figure


class Quadrik(Figure):

    def __init__(self, x1, y1, x2, y2, x3, y3):
        super().__init__()
        self._vertex1 = (x1, y1)
        self._vertex2 = (x2, y2)
        self._vertex3 = (x3, y3)

    def draw(self):
        v0 = self.calc_absolute_position((0, 0))
        v1 = self.calc_absolute_position(self._vertex1)
        v2 = self.calc_absolute_position(self._vertex2)
        v3 = self.calc_absolute_position(self._vertex3)
        up()
        pencolor(self._color)
        setpos(*v0)
        down()
        goto(*v1)
        goto(*v2)
        goto(*v3)
        goto(*v0)
        up()


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
        t = Quadrik(x1, y1, x2, y2, x3, y3)
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
