# Визначити загальну кількість операцій додавання (+), віднімання (-)
#  та множення (*) у заданому арифметичному виразі.

expr = input()
counter = 0
for c in expr[1:]:
    if c in "+-*":
    # if c == "+" or c == "-" or c == "*":
        counter += 1
print(counter)