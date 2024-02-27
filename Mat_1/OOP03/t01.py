import turtle # Підключаємо модуль turtle
import math

if __name__ == '__main__':
    turtle.reset()
    turtle.speed(1)
    turtle.setpos(100, 100)
    turtle.down()
    turtle.forward(50)
    turtle.right(45)
    turtle.forward(100)
    turtle.goto(0, 0)
    turtle.up()

    turtle.mainloop()