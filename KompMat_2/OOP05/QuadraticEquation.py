from Equation import Equation
class QuadraticEquation(Equation):
    def __init__(self, a, b, c):
        super().__init__(b, c)
        self.a = a

    def __str__(self):
        return f"{self.a}x**2 + " + super().__str__()

    def discr(self):
        return self.b ** 2 - 4 * self.a * self.c

    def solve(self):
        if self.a == 0:
            return super().solve()
        else: # a != 0 - звичайне квадратне рівняння
            d = self.discr()
            if d < 0:
                return ()
            elif d == 0:
                x1 = - self.b / (2 * self.a)
                return (x1, )
            else: # d > 0
                d_sqr = d ** 0.5
                x1 = (- self.b + d_sqr) / (2 * self.a)
                x2 = (- self.b - d_sqr) / (2 * self.a)
                return (x1, x2)


if __name__ == '__main__':
    e = QuadraticEquation(0, 5, 4)
    print(e)
    print(e.solve())

    e = QuadraticEquation(0, 0, 4)
    print(e)
    print(e.solve())

    e = QuadraticEquation(0, 0, 0)
    print(e)
    print(e.solve())

    e = QuadraticEquation(0, 5, 0)
    print(e)
    print(e.solve())

    e = QuadraticEquation(1, 3, 8)
    print(e)
    print(e.solve())

    e = QuadraticEquation(1, 4, 4)
    print(e)
    print(e.solve())

    e = QuadraticEquation(1, -3, 2)
    print(e)
    print(e.solve())

    e = QuadraticEquation(2, -6, 4)
    print(e)
    print(e.solve())


