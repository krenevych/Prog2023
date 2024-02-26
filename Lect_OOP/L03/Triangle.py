import copy
class Triangle:
    def __init__(self, a, b, c):
        assert a + b > c and a + c > b and b + c > a
        self.__a = a
        self.__b = b
        self.__c = c

    def set_a(self, a):
        if a + self.__b > self.__c and a + self.__c > self.__b and self.__b + self.__c > a:
            self.__a = a
        else:
            print("set_a: Error")

    def set_b(self, b):
        if self.__a + b > self.__c and self.__a + self.__c > b and b + self.__c > self.__a:
            self.__b = b

    def set_c(self, c):
        if self.__a + self.__b > c and self.__a + c > self.__b and self.__b + c > self.__a:
            self.__c = c

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def perimeter(self):
        return (self.__a + self.__b + self.__c) / 2

    def area(self):
        p = self.perimeter()
        return (p * (p - self.__a) * (p - self.__b) * (p - self.__c))**0.5

    def show(self):
        print("Triangle", self.__a, self.__b, self.__c)


if __name__ == '__main__':
    try:
        t = Triangle(3, 4, 5)
        t.show()
        t.set_a(4)
        t.show()


        print("Area = ", t.area())
    except AssertionError:
        print("Triangle isn't exist")

