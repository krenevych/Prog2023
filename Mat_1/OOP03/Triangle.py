from turtle import *


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


if __name__ == '__main__':
    t = Triangle(100, 50, -200, 100)
    t.draw()
    clear()
    t.translate(-100, -200)
    t.draw()

    mainloop()
