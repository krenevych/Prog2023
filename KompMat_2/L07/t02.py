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
    elif n == 5:
#         Обчислити суму
#         двозначних чисел, цифри яких парні.
        if od % 2 == 0 and de % 2 == 0:
            counter += i


print(counter)
