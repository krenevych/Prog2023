# Знайти суму цифр заданого натурального числа.

# 256 = 2 * 100 + 5 * 10 + 6
# 256 = 2 * 10**2 + 5 * 10**1 + 6 * 10**0

N = 256

# suma = 0
while N > 0:
    last = N % 10
    # suma += last
    N = N // 10
