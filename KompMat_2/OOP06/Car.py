import turtle

from Figure import Figure
from Triangle import Triangle
from Circle import Circle
from  Rectangle import Rectangle


class Car(Figure):

    def __init__(self):
        super().__init__()
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def draw(self):
        for component in self.components:
            component.position = self.position

        for component in self.components:
            component.draw()


if __name__ == '__main__':
    body = Rectangle(200, 100)
    window = Triangle(50, 100, 150, 100, 125, 150)
    wheel1 = Circle(20, 35, -25)
    wheel2 = Circle(20, 165, -25)

    car = Car()
    car.add_component(body)
    car.add_component(window)
    car.add_component(wheel1)
    car.add_component(wheel2)

    turtle.speed(0)
    for step in range(1, 100, 10):
        # car.move(10, 0)
        car.set_scale(1 + step / 10, 1 + step / 10)
        car.draw()
        turtle.clear()

    turtle.mainloop()
