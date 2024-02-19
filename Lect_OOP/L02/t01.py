import copy
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return (self.a + self.b + self.c) / 2

    def area(self):
        p = self.perimeter()
        return (p * (p - self.a) * (p - self.b) * (p - self.c))**0.5

    def show(self):
        print("Triangle", self.a, self.b, self.c)


if __name__ == '__main__':
    t = Triangle(3, 4, 5)
    t1 = copy.copy(t)
    t2 = copy.deepcopy(t)
    t1.a = 4
    t.show()
    t1.show()

