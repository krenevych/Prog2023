s = input() # -1+2*3+a
counter = 0
for c in s[1:]:
    # if c == "+" or c == "-" or c == "*":
    if c in "+-*":
        counter +=1
    # print(c)
print(counter)
