# Скільки разів кожна цифра входить в число

d = 123904875722345172395
freq = [0] * 10
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#  0  1  2  3  4  5  6  7  8  9
while d > 0:
    cur = d % 10
    freq[cur] += 1
    d = d // 10

# print(freq)

# for el in freq:
#     print(el)

# for i in range(len(freq)):
#     print(f"{i}: {freq[i]}")

for i, el in enumerate(freq):
    print(f"{i}: {el}")


