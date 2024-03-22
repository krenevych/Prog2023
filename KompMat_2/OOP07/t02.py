class Integer:
    def __init__(self, a):
        assert type(a) == int
        self.a = a

    def __str__(self):
        return f"Integer: {self.a}"

    def __add__(self, other):
        return Integer(self.a + other.a)


print(Integer(7) + Integer(4))


class Rational(Integer):
    def __init__(self, a, b=1):
        if type(a) == Rational:
            super().__init__(a.a)
            self.b = a.b
        else:
            super().__init__(a)
            assert b != 0 and type(b) == int
            self.b = b

    def __str__(self):
        return f"Rational: {self.a}/{self.b}"

    def __add__(self, other):
        # if isinstance(other, Integer): - бо кіт це і кіт і тварина :)

        if type(other) == Integer:
            return Rational(self.a + other.a * self.b, self.b)

        if type(other) == Rational:
            num = self.a * other.b + self.b * other.a
            den = self.b * other.b
            return Rational(num, den)


print(Rational(2, 3) + Integer(7) + Rational(15, 2))
