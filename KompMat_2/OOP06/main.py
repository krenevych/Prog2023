from Triangle import Triangle
from Rectangle import Rectangle
import turtle

if __name__ == '__main__':
    body = Rectangle(200, 100)
    window = Triangle(100, 0, 50, 100)
    window.set_position(50, 100)

    body.draw()
    window.draw()

    turtle.mainloop()