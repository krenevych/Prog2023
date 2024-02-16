class Triangle:
    def __init__(self, a: float, b: float, c: float):
        edges = [a, b, c]
        edges.sort()
        a, b, c = edges
        assert a + b > c
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return (self.a + self.b + self.c) / 2

    def area(self) -> float:
        p = self.perimeter()
        return (p * (p - self.a) * (p - self.b) * (p - self.c))**0.5

    def __str__(self) -> str:
        return f"Tringle: a={self.a}, b={self.b}, c={self.c}"

if __name__ == '__main__':
    t = Triangle(3,4,5)
    print(t.area())
