# https://www.eolymp.com/uk/problems/8990
# welcome to python
s = input()  # welcome to python
new = ""
for c in s:
    # print(c)
    new = new + c # new += c
    if c in "aeiouy":
        new += c


print("new :",new)