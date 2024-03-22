class Integer:
    def __init__(self, a):
        assert type(a) == int
        self.a = a

    def print(self):
        print(self.a)

    def add(self, other):
        return Integer(self.a + other.a)


i1 = Integer(7)
i2 = Integer(4)
i_res = i1.add(i2)


class Rational(Integer):
    def __init__(self, a, b=1):
        if type(a) == Rational:
            super().__init__(a.a)
            self.b = a.b
        else:
            super().__init__(a)
            assert b != 0 and type(b) == int
            self.b = b

    def print(self):
        print(f"{self.a}/{self.b}")

    def add(self, other):
        # if isinstance(other, Integer): - бо кіт це і кіт і тварина :)

        if type(other) == Integer:
            return Rational(self.a + other.a * self.b, self.b)

        if type(other) == Rational:
            num = self.a * other.b + self.b * other.a
            den = self.b * other.b
            return Rational(num, den)


r1 = Rational(2, 3)
i3 = Integer(7)
r2 = Rational(15, 2)

res = r1.add(i3).add(r2)

res.print()
