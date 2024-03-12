from Equation import Equation
class QuadraticEquation(Equation):
    def __init__(self, a, b, c):
        super().__init__(b, c)
        self.a = a

    def __str__(self):
        return f"{self.a}x**2 + " + super().__str__()


if __name__ == '__main__':
    e = QuadraticEquation(1, 2, 3)
    print(e)
