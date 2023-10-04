# https://www.e-olymp.com/uk/problems/7599
n = int(input())
counter = 0
for i in range(10, 100):
    od = i % 10
    de = i // 10

    if n == 1:  # n=1: Обчислити кiлькiсть
        # двозначних чисел, цифри яких спадають.
        if de > od:
            counter += 1

    elif n == 2:  # n=2: Обчислити кiлькiсть двозначних чисел,
        # цифри яких зростають.
        pass
    elif n == 3:
        pass
    elif n == 4:
        pass
    elif n == 5:
        pass
    else:
        pass


print(counter)

