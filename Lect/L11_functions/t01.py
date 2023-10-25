# опишемо функцію, що буде шукати більше з двох чисел
def max2(a, b):
    if a > b:
        return a

    return b


m = max2(max2(41, 5), 13)
print(m)
