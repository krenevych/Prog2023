from Figure import Figure

import turtle

class Rectangle(Figure):

    def __init__(self, x1, y1, x2=0, y2=0):
        super().__init__()
        self._vertex1 = (x1, y1)
        self._vertex2 = (x2, y2)

    def draw(self):
        v0 = self.calc_abs_pos((self._vertex1[0], self._vertex1[1]))
        v1 = self.calc_abs_pos((self._vertex2[0], self._vertex1[1]))
        v2 = self.calc_abs_pos((self._vertex2[0], self._vertex2[1]))
        v3 = self.calc_abs_pos((self._vertex1[0], self._vertex2[1]))
        turtle.color(self.color)
        turtle.up()
        turtle.goto(*v0)
        turtle.down()
        turtle.goto(*v1)
        turtle.goto(*v2)
        turtle.goto(*v3)
        turtle.goto(*v0)
        turtle.up()
        turtle.color(Rectangle.default_color)



if __name__ == '__main__':
    turtle.speed(0)
    figure = Rectangle(100, 100)
    figure.draw()

    for step in range(1, 100):
        figure.set_rotation_degree(step)
        # figure.move(step, step)
        figure.set_scale(1 + step / 20, 1 + step /20)
        figure.draw()
        turtle.clear()

    turtle.mainloop()