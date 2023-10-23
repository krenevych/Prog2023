# Без повторень 3
# https://www.e-olymp.com/uk/problems/8992


s = input()  # WWWellcccooomee  ttoo PPyythooonn!!!
new = s[0]
for c in s[1:]:
    if c != new[-1]:
        new += c

print("new :",new)