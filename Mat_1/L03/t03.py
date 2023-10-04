# На вході програми маємо послідовність цілих чисел,
# що закінчується числом 0.

# a = int(input())
# while a != 0:
#     print(a)
#     a = int(input())

# Потрібно знайти довжину даної послідовності,
# не враховуючи останнього нуля.
counter = 0
while True:
    a = int(input())
    if a == 0:
        break
    counter += 1

print(counter)
