from turtle import *
from random import randint


class Triangle:

    def __init__(self, x1, y1, x2, y2):
        self._vertex1 = (x1, y1)
        self._vertex2 = (x2, y2)
        self._position = (0, 0)

    def translate(self, dx, dy):
        self._position = (self._position[0] + dx,
                          self._position[1] + dy)

    def set_position(self, x, y):
        self._position = (x, y)

    def calc_absolute_position(self, vertex):
        x = self._position[0] + vertex[0]
        y = self._position[1] + vertex[1]
        return x, y


    def draw(self):
        v0 = self.calc_absolute_position((0, 0))
        v1 = self.calc_absolute_position(self._vertex1)
        v2 = self.calc_absolute_position(self._vertex2)
        up()
        setpos(*v0)
        down()
        goto(*v1)
        goto(*v2)
        goto(*v0)
        up()

def createTriangles(number):
    # генерація випадкового числа з проміжку  [0, 10]
    bound = 350
    triangles = []
    for i in range(number):
        x1 = randint(-bound, bound)
        y1 = randint(-bound, bound)
        x2 = randint(-bound, bound)
        y2 = randint(-bound, bound)
        t = Triangle(x1, y1, x2, y2)
        triangles.append(t)
    return triangles

if __name__ == '__main__':
    triangles = createTriangles(5)
    for t in triangles:
        bound = 100
        x0 = randint(-bound, bound)
        y0 = randint(-bound, bound)
        t.set_position(x0, y0)
        t.draw()

    mainloop()
