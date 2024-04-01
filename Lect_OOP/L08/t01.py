class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        if type(other) == Complex:
            self.x += other.x
            self.y += other.y
        elif type(other) == int or type(other) == float:
            self.x += other
        elif type(other) == complex:
            self.x += other.real
            self.y += other.imag
        return self

    def __sub__(self, other):
        return Complex(self.x - other.x, self.y - other.y)

    def __truediv__(self, other):
        return Complex(self.x / other.x, self.y / other.y) # з точки зору математики не правильна формула,
                                                           # використовуємо її, щоб не ускладнювати код
    def __mul__(self, other):
        res = self.x * other.x + self.y * other.y # операцію множення робимо як скалярний добуток двох двовимірних векторів
                                                  # з точки зору комплексного аналізу це не правильна поведінка
        return res

    def __abs__(self):
        res = (self.x**2 + self.y**2)**0.5
        return res

    def __bool__(self):
        return not(self.x == 0 and self.y == 0)

    def __str__(self):
        return f"Complex: {self.x} + {self.y}i"

    def __int__(self):
        return int(self.x)

    def __float__(self):
        return float(self.x)

    def __complex__(self):
        return complex(self.x, self.y)

    def __eq__(self, other):
        if type(other) == Complex:
            return self.x == other.x and self.y == other.y
        if type(other) == int:
            return self.x == other and self.y == 0

        if type(other) == complex:
            return self.x == other.real and self.y == other.imag

    def __neg__(self):
        res = Complex(-self.x, -self.y)
        return res

if __name__ == '__main__':

    z = Complex(3, 4)
    z2 = -z
    print(z)
    print(z2)