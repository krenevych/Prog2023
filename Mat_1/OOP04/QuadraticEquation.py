from Equation import Equation


class QuadraticEquation(Equation):

    def __init__(self, a, b, c):
        super().__init__(b, c)
        self.a = a

    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def solve(self):
        if self.a == 0:
            return super().solve()
        else: # a != 0
            d = self.discriminant()
            if d < 0:
                return ()
            elif d == 0:
                x1 = -self.b / (2 * self.a)
                return (x1,)
            else:
                d2 = d ** 0.5
                x1 = (-self.b - d2) / (2 * self.a)
                x2 = (-self.b + d2) / (2 * self.a)
                return x1, x2

    def __str__(self):
        return f"{self.a}x**2 + {self.b}x + {self.c} = 0"

if __name__ == '__main__':
    eq1 = QuadraticEquation(0, 2, 3)
    print(eq1)
    print(eq1.solve())
    eq2 = QuadraticEquation(0, 0, 0)
    print(eq2)
    print(eq2.solve())
    eq3 = QuadraticEquation(0, 0, 5)
    print(eq3)
    print(eq3.solve())

    eq1 = QuadraticEquation(1, -3, 2)
    print(eq1)
    print(eq1.solve())
    eq2 = QuadraticEquation(1, 2, 1)
    print(eq2)
    print(eq2.solve())
    eq3 = QuadraticEquation(1, 1, 5)
    print(eq3)
    print(eq3.solve())
    eq7 = QuadraticEquation(4, 1, -5)
    print(eq7)
    print(eq7.solve())
    eq8 = QuadraticEquation(1, 1, 1)
    print(eq8)
    print(eq8.solve())



