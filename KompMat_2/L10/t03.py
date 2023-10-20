s = input() # welcome to python

new = ""
for c in s:
    new  = new + c
    if c in "aeuoyi":
        new += c
print(new)

