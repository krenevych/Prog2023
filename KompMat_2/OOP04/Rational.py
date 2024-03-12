class Rational:
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def print(self):
        print(f"{self.n}/{self.d}")

    def add(self, other):
        n = self.n * other.d + other.n * self.d
        d = self.d * other.d
        return Rational(n, d)

    def mult(self, n):
        n = self.n * n
        return Rational(n, self.d)


r1 = Rational(2, 3)
r2 = Rational(7, 6)
r3 = Rational(2, 7)
r4 = r2.mult(5)
r5 = r3.mult(3)
r = r1.add(r4).add(r5)
r.print()
