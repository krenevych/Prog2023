class Triangle:
    def __init__(self, a, b, c):
        edges = [a, b, c]
        edges.sort()
        a, b, c = edges
        assert a + b > c
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return (self.a + self.b + self.c) / 2

    def area(self):
        p = self.perimeter()
        return (p * (p - self.a) * (p - self.b) * (p - self.c))**0.5


if __name__ == '__main__':
    t = Triagle(3,4,5)
    print(t.area())
