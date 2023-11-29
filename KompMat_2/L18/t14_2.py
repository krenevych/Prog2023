s = input("введіть рядок")
suma = 0
for c in s:
    # if c >= '0' and c <= '9':
    # if c.isdigit():
    try:
        suma += int(c)
    except ValueError:
        pass

print(suma)