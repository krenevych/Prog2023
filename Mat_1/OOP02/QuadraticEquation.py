class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.d = b**2 - 4 * a * c

    def show(self):
        print(f"{self.a}x^2 + {self.b}x + {self.c} = 0")


if __name__ == '__main__':
    eq = QuadraticEquation(1, 4, -4)
    eq.show()
    print(eq.d)
    eq.a = 15
    eq.show()
    print(eq.d)
    eq.d = -100500
    print(eq.d)
