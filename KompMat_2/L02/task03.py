# Програма зчитує двоцифрове число і виводить
# через пропуск кожну цифру окремо.

x = int(input())   # int - цілі. float - дійсні
# x = 23

odinytsi = x % 10
desyatky = x // 10

print(desyatky, odinytsi)
