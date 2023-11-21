# Задано послідовність дійсних невід’ємних чисел.
# Знайдемо максимум відношень між сусідніми членами цієї послідовності.
# 1 3 12 89 6 1
seq = [1, 3, 12, 84, 6, 1]
max_ratio = 0
try:
    for i in range(1, len(seq)):
        cur_ratio = seq[i] / seq[i-1]
        if cur_ratio > max_ratio:
            max_ratio = cur_ratio
    print("Максимальне відношення:", max_ratio)
except ZeroDivisionError:
    print("Послідовність містить нуль!!")
# else:
#     print("Максимальне відношення:", max_ratio)



