class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        # self.d = self.b**2 - 4 * self.a * self.c - Dont do this because...

    def discrim(self):
        d = self.b**2 - 4 * self.a * self.c
        return d

    INF = "INF"
    def solutions(self): # повертає список розвʼязків рівння або "INF", якщо рівняння має нескінченну кількість розвʼязків
        if self.a == 0:  # Лінійне рівняння
            if self.b != 0: # 3x + 5 = 0 => один розвʼязок -c / b
                x1 = -self.c / self.b
                return [x1]
            else: # b = 0
                if self.c != 0: # 5 = 0 => розвʼязків немає
                    return []
                else:  # 0 = 0  => безліч рівнянь
                    return QuadraticEquation.INF
        else:          # a != 0 Квадратне рівняня
            d = self.discrim()
            if d < 0:  # розвʼязків немає
                return []
            elif d == 0: # один розвʼязок
                x1 = -self.b / (2 * self.a)
                return [x1]
            else: # d > 0 # два розвʼязки
                d2 = d ** 0.5
                x1 = (-self.b - d2)/ (2 * self.a)
                x2 = (-self.b + d2)/ (2 * self.a)
                sol = [x1, x2]
                sol.sort()
                return sol

###############################
if __name__ == '__main__':
    eq = QuadraticEquation(0, 0, 0)
    print(eq.a, eq.b, eq.c)

    print(eq.solutions())
