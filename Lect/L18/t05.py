# Порахуємо площу трикутника за трьома сторонами
def triangleSquare(a, b, c):
    assert a + b > c and a + c > b and c + b > a, "AssertionError: Не виконується нерівність трикутника"
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s


a = 3
b = 4
c = 15
try:
    print(triangleSquare(a, b, c))
except AssertionError as err:
    print(err)