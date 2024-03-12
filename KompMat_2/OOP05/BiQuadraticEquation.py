from QuadraticEquation import QuadraticEquation

class BiQuadraticEquation(QuadraticEquation):

    def __str__(self):
        return f"{self.a}x^4 + {self.b}x^2 + {self.c} = 0"

    def solve(self):
        set_solutions = set() # множина розвʼязків => потім перетворимо результат у кортеж
        solutions_quadratic = super().solve()
        if solutions_quadratic == BiQuadraticEquation.INF:
            return BiQuadraticEquation.INF
        for solution in solutions_quadratic:
            if solution >= 0:
                t1 = solution ** 0.5
                t2 = -t1
                set_solutions.add(t1)
                set_solutions.add(t2)

        return tuple(set_solutions)

if __name__ == '__main__':
    e = BiQuadraticEquation(0, 5, 4)
    print(e)
    print(e.solve())

    e = BiQuadraticEquation(0, 0, 4)
    print(e)
    print(e.solve())

    e = BiQuadraticEquation(0, 0, 0)
    print(e)
    print(e.solve())

    e = BiQuadraticEquation(0, 5, 0)
    print(e)
    print(e.solve())

    e = BiQuadraticEquation(1, 3, 8)
    print(e)
    print(e.solve())

    e = BiQuadraticEquation(1, 4, 4)
    print(e)
    print(e.solve())

    e = BiQuadraticEquation(1, -3, 2)
    print(e)
    print(e.solve())

    e = BiQuadraticEquation(2, -6, 4)
    print(e)
    print(e.solve())

    e = BiQuadraticEquation(1, 0, 0)
    print(e)
    print(e.solve())


