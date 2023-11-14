# У текстовому файл містить набір чисел,
# кожне з яких записано з нового рядка.
# Потрібно знайти cуму цих чисел.

f = open("input06.txt", encoding="utf-8")
numbers = [float(line) for line in f.readlines()]
f.close()

print(sum(numbers))
