from Triangle import Triangle
from Rectangle import Rectangle
from Circle import Circle
import turtle

if __name__ == '__main__':
    body = Rectangle(200, 100)
    window = Triangle(100, 0, 50, 100)
    window.set_position(50, 100)
    wheel1 = Circle(20)
    wheel2 = Circle(20)
    wheel1.set_position(35, -25)
    wheel2.set_position(165, -25)
    wheel1.draw()
    wheel2.draw()

    body.draw()
    window.draw()

    turtle.mainloop()