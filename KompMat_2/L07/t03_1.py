# На вході програми маємо послідовність цілих чисел,
# що закінчується числом 0.
counter = 0
a = int(input())
while a != 0:
    a = int(input())
    counter += 1

print(counter)