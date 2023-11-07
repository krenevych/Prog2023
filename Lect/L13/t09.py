# while True:
#     lst = input().split()
#     if len(lst) != 2:
#         break
#     n, m = [int(el) for el in lst]
#     print(n, m)


# while True:
#     try:
#         n, m = [int(el) for el in input().split()]
#     except:
#         break
#     print(n, m)

with open("input.txt") as f:
    for line in f:
        n, m = [int(el) for el in line.split()]
        print(n, m)

