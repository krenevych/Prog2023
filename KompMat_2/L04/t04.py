n = int(input())
counter = 0
if n == 0:
    counter += 1
else:
    while n > 0:
        # print("зʼїв шматок піци")
        counter += 1
        n = n // 10

print(counter)