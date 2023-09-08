x = int(input())
x = abs(x)
# x = 198
# x = -232
firstnum = x % 10
secnum = x // 10 % 10
thirdnum = x // 100
print(thirdnum)
print(secnum)
print(firstnum)
