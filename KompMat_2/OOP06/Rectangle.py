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
    triangle = Rectangle(100, 100)
    triangle.draw()

    for degree in range(3, 363, 3):
        triangle.set_rotation_degree(degree)

        triangle.draw()
        turtle.clear()

    turtle.mainloop()