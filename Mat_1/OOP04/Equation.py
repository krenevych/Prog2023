class Equation:
    """
    клас Equation (Рівняння), що моделює лінійне алгебраїчне рівняння виду
                    bx+c=0.
    """
    INF = "infinity"

    def __init__(self, b, c):
        self.b = b
        self.c = c

    def solve(self):
        if self.b != 0:
            x1 = -self.c / self.b
            return (x1, )
        else: # b == 0
            if self.c == 0: # 0 == 0
                return Equation.INF
            else: # 0 == 10
                return ()

    def __str__(self):
        return f"{self.b}x + {self.c} = 0"

if __name__ == '__main__':
    eq1 = Equation(2, 3)
    print(eq1)
    print(eq1.solve())
    eq2 = Equation(0, 0)
    print(eq2)
    print(eq2.solve())
    eq3 = Equation(0, 5)
    print(eq3)
    print(eq3.solve())
