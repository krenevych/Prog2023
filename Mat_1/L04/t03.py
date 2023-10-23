# https://www.eolymp.com/uk/problems/919
N = int(input())
lst = [float(el) for el in input().split()]
# print(lst)
suma = 0
count = 0
# for i in range(N):
#     el = lst[i]
#
#     if (i + 1) % 3 == 0 and el > 0:
#         suma += el
#         count +=1
# for i in range(2, N, 3):
#     el = lst[i]
#
#     if el > 0:
#         suma += el
#         count +=1
# print(count, suma)

for el in lst[2::3]:
    if el > 0:
        suma += el
        count +=1
print(count, suma)

