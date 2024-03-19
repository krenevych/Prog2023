class Real:
    def __init__(self, x):
        self.x = x

    def print(self):
        print(self.x)

    def add(self, other):
        return Real(self.x + other.x)


class Complex(Real):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def print(self):
        print(f"{self.x}+{self.y}i")

    def add(self, other):

        if isinstance(other, Complex):
            return Complex(self.x + other.x, self.y + other.y)

        if isinstance(other, Real):
            return Complex(self.x + other.x, self.y)


z1 = Complex(3, 4)
z2 = Real(12)
z3 = Complex(7, 3)

res = z1.add(z2)
res = res.add(z3)
res.print()










