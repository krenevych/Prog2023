# Дано масив з N цілих чисел.
# Визначте, скільки в цьому масиві різних елементів.
N = int(input())
digits = {int(el) for el in input().split()}
print(len(digits))
