class Rational:
    def __init__(self, n, d=1):
        assert type(n) == int
        assert d != 0 and type(d) == int
        self.n = n
        self.d = d

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __add__(self, other):
        num = self.n * other.d + self.d * other.n
        den = self.d * other.d
        return Rational(num, den)

    def __call__(self):
        return self.n/self.d

r1 = Rational(2, 3)
r2 = Rational(4, 5)
r3 = Rational(15, 26)

# res = r1.add(r2).add(r3)
res = r1 + r2 + r3

print(res)
print(res())
