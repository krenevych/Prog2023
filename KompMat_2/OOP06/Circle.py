from Figure import Figure

import turtle

class Circle(Figure):

    def __init__(self, r):
        super().__init__()
        self._r = r

    def draw(self):
        s = self._r * self.scale[1]
        v1 = self.position[0], self.position[1] - s

        turtle.color(self.color)
        turtle.up()
        turtle.setpos(*v1)
        turtle.down()
        turtle.circle(s)
        turtle.up()
        turtle.color(Circle.default_color)



if __name__ == '__main__':
    turtle.speed(0)
    figure = Circle(100)
    figure.draw()

    for step in range(1, 100):
        figure.set_scale(1 + step / 20, 1 + step /20)
        figure.draw()
        turtle.clear()

    turtle.mainloop()