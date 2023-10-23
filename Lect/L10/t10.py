# Обчислити кількість входжень символа a у рядок s

S = "Hello world! Hello, hello, HELLO"
ch = "l"
counter = 0
for d in S:
    if ch == d:
        counter += 1
print(counter)
