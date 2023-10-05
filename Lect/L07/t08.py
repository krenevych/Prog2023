lst = [el**2 for el in range(1, 100)
       if (el % 2 == 1 and el % 3 == 0)]

print(lst)

lst2 = [el for el in "Hello, world"
       if el in "eoiauy"]

print(lst2)


