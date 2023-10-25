def max(*args):
    if len(args) == 0:
        return None
    m = args[0]  # m - локальна змінна, яка не видима з головної програми
    for el in args[1:]:
        if el > m:
            m = el
    print(m)
    return m


# print(m) # якщо розкоментувати буде помилка, бо m - не видима з головної програми