import turtle
from random import randint
from Triangle import Triangle
# генерація випадкового числа з проміжку  [0, 10]

triangles = []
for i in range(2):
    x1 = randint(-100, 100)
    y1 = randint(-100, 100)
    x2 = randint(-100, 100)
    y2 = randint(-100, 100)
    t = Triangle(x1, y1, x2, y2)

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(15, 255)
    color = r << 16 | g << 8 | b
    t.set_color("#" + str(hex(color))[2:])

    triangles.append(t)

for t in triangles:
    t.draw()

turtle.mainloop()




