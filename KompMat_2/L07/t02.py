# Обчислити кiлькiсть двозначних чисел,
# цифри яких спадають.
n = int(input())
counter = 0
for i in range(10, 100):
    # print(i)
    od = i % 10
    de = i // 10
    if n == 1:
        if od < de:
            counter += 1
    elif n == 2:
        pass
    elif n == 3:
        pass

print(counter)
