N = int(input())
lst = [int(el) for el in input().split()]
# print(lst)
# maximum = lst[0]
# 5 9 3 4 6
# for el in lst[1:]:
#     if maximum < el:
#         maximum = el

# for i in range(1, N):
#     el = lst[i]
#     if maximum < el:
#         maximum = el
maximum = max(lst)
print(maximum)