import random

def ispow5(a):
    while a > 1:
        if a % 5 != 0:
            return False
        a = a // 5
    return True

print(
    ispow5(626)
)

lst = []
for i in range(100):
    lst.append(random.randint(1, 1000))

for el in lst:
    if ispow5(el):
        print(el)

# print(lst)
