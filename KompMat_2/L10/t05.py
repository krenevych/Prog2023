s = input()

new = s[0]
for c in s[1:]:
    if c != new[-1]:
        new += c

print(new)