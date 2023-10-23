# Голосні
# https://www.e-olymp.com/uk/problems/494



expr = input()
counter = 0
for c in expr:
    if c in "AEIOUY":
    # if c == "+" or c == "-" or c == "*":
        counter += 1
print(counter)