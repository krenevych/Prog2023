# На вході програми маємо послідовність цілих чисел,
# що закінчується числом 0.
counter = 0
while True:
    a = int(input())
    if a == 0:
        break
    counter += 1

print(counter)