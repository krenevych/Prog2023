collection = [1, 2, 3, 4, 55, 66, 55, 33, 33]

d = dict.fromkeys(collection, 0)

print(d)

s = "hello, world"
d = dict.fromkeys([chr(c) for c in range(ord("a"), ord("a") + 26)], 0)
print(d)

