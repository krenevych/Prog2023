# Для заданого натурального числа n
# виведіть його найменший дільник, відмінний від 1.
n = int(input())

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        print(i)
        break
else:
    print(n)
