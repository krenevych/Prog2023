class Complex(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        res = (self.x**2 + self.y**2)**0.5
        return res

    def __bool__(self):
        return not(self.x == 0 and self.y == 0)
        # if self.x == 0 and self.y == 0:
        #     return False
        # else:
        #     return True

    def __str__(self):
        return f"Complex: {self.x} + {self.y}i"

    def __int__(self):
        return int(self.x)

    def __float__(self):
        return float(self.x)

    def __complex__(self):
        return complex(self.x, self.y)

z = Complex(3, 4)
# z = Complex(0, 0)
# print(bool(z))
print(abs(z))
z_str = str(z)
print(z)

print(int(z))
print(float(z))
print(complex(z))
