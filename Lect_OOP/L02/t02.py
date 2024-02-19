from random import random, randint


class Triangle:

    triangle_id = 0  # статичне поле класу
    @staticmethod  # декоратор, що позначає, що зараз відбувається опис статичного методу
    def get_triangle_id():
        return Triangle.triangle_id

    @staticmethod  # декоратор, що позначає, що зараз відбувається опис статичного методу
    def gen_triangle_id():
        return randint(1, 1000000)

    def __init__(self, a, b=None, c=None):

        if isinstance(a, Triangle):
            self.a = a.a
            self.b = a.b
            self.c = a.c
        else:
            self.a = a
            self.b = b
            self.c = c

        self.id = Triangle.triangle_id
        Triangle.triangle_id += 1

    def perimeter(self):
        return (self.a + self.b + self.c) / 2

    def area(self):
        p = self.perimeter()
        return (p * (p - self.a) * (p - self.b) * (p - self.c))**0.5

    def show(self):
        print("Triangle, id = ",self.id, "edges:", self.a, self.b, self.c)


if __name__ == '__main__':
    # t = Triangle(3, 4, 5)
    # t3 = Triangle(t)
    # t.show()
    # t3.show()
    print(Triangle.triangle_id)
    print(Triangle.get_triangle_id())
    print(Triangle.gen_triangle_id())



