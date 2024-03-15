from Figure import Figure

import turtle

class Rectangle(Figure):

    def __init__(self, x1, y1):
        super().__init__()
        self._vertex1 = (x1, y1)

    def draw(self):
        v1 = self.calc_abs_pos((self._vertex1[0], 0))
        v2 = self.calc_abs_pos(self._vertex1)
        v3 = self.calc_abs_pos((0, self._vertex1[1]))
        turtle.color(self.color)
        turtle.up()
        turtle.setpos(*self.position)
        turtle.down()
        turtle.goto(*v1)
        turtle.goto(*v2)
        turtle.goto(*v3)
        turtle.setpos(*self.position)
        turtle.up()
        turtle.color(Rectangle.default_color)



if __name__ == '__main__':
    turtle.speed(0)
    figure = Rectangle(100, 100)
    figure.draw()

    for step in range(1, 100):
    # for degree in range(3, 363, 3):
        # figure.set_rotation_degree(degree)
        # figure.move(degree, degree)
        figure.set_scale(1 + step / 20, 1 + step /20)
        figure.draw()
        turtle.clear()

    turtle.mainloop()