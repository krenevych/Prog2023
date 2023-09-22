n = int(input())
suma = 0
dodu = 1
while n > 0:
    last = n % 10
    suma += last
    dodu *= last
    n = n // 10

res =  dodu / suma
print(f"{res:0.3f}")
