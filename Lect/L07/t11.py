
lst = [1, 3, 1, 2, 9, 1, 7, 8, 9, 10, 11, 12, 13]
#      0  1  2  3  4  5  6  7  8  9   10  11  12
#              -10-9 -8 -7 -6  -5 -4  -3  -2  -1
lst1 = lst[:5]
print(lst1)

# lst2 = lst[-10: -2]
lst2 = lst[3: -2]
print(lst2)
listWithoutFirstAndLast = lst[1:-1]
print(listWithoutFirstAndLast)



