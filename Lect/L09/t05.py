# Переверніть масив чисел.

N = int(input())
# lst = []
# for i in range(N):
#     a = int(input())
#     lst.append(a)

lst = [0] * N
for i in range(N):
    lst[i] = int(input())

# print(*lst[::-1])  # реверс використовуючи операцію зріз

# [4 3 2 1 5]
#  0 1 2 3 4

for i in range(N // 2):
    # a = lst[i]
    # lst[i] = lst[-1 - i]
    # lst[-1 - i] = a
    lst[i], lst[-1 - i] = lst[-1 - i], lst[i]

print(*lst)
