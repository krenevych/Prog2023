lst1 = [1, 3, 5]
#       0  1  2
print(lst1)
# lst1.append(7)
# print(lst1)

# lst1[len(lst1):len(lst1)]
# lst1[1:1] = [22] # вставка елементу 22
# lst1[1:1] = [22, 33, 44] # вставка елементів 22, 33, 44
lst1[len(lst1):len(lst1)] = [22] # додавання елементу 22 в кінець = append
print(lst1)
lst1[len(lst1):len(lst1)] = [33, 44, 55] # extend
print(lst1)

