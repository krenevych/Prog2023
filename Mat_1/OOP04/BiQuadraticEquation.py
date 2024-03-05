from QuadraticEquation import QuadraticEquation


class BiQuadraticEquation(QuadraticEquation):

    # конструктор не оголошуємо, бо наслідується
    # конструктор з класу QuadraticEquation, де все вже є

    def solve(self):
        solutions_of_quad = super().solve()
        if solutions_of_quad == BiQuadraticEquation.INF:
            return QuadraticEquation.INF

        result_solutions = set()
        for sol in solutions_of_quad:
            if sol < 0:
                continue
            x1 = sol ** 0.5
            x2 = -x1
            result_solutions.add(x1)
            result_solutions.add(x2)

        return tuple(result_solutions)

    def __str__(self):
        return f"{self.a}x**4 + {self.b}x**2 + {self.c} = 0"


if __name__ == '__main__':
    eq1 = BiQuadraticEquation(0, 2, 3)
    print(eq1)
    print(eq1.solve())
    eq2 = BiQuadraticEquation(0, 0, 0)
    print(eq2)
    print(eq2.solve())
    eq3 = BiQuadraticEquation(0, 0, 5)
    print(eq3)
    print(eq3.solve())

    eq1 = BiQuadraticEquation(1, -3, 2)
    print(eq1)
    print(eq1.solve())
    eq2 = BiQuadraticEquation(1, 2, 1)
    print(eq2)
    print(eq2.solve())
    eq3 = BiQuadraticEquation(1, 1, 5)
    print(eq3)
    print(eq3.solve())
    eq7 = BiQuadraticEquation(4, 1, -5)
    print(eq7)
    print(eq7.solve())
    eq8 = BiQuadraticEquation(1, 1, 1)
    print(eq8)
    print(eq8.solve())

