class Vector:

    r = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'Vector({self.x}, {self.y})'
    def __add__(self, other):
        if isinstance(other, Vector):
            x = self.x + other.x
            y = self.y + other.y
            return Vector(x, y)
        elif isinstance(other, float) or isinstance(other, int):
            x = self.x + other
            y = self.y
            return Vector(x, y)


v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # v3 = v1.__add__(v2)
# print(v1)
# print(v2)
# # v3 = Vector.add(v1, v2)
# v3 = v1 + v2
# print(v3)

# print(v1 + 6)

print(v3.__dict__)
print(Vector.__dict__)


