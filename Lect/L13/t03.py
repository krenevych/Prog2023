# lst = [int(el) for el in input().split()]
lst = input().split()

def myConverter(elem):
    return int(elem) ** 2

# lst2 = list(map(int, lst))
lst2 = list(map(myConverter, lst))

print(lst2)