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

if __name__ == '__main__':
    pass



