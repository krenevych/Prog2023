s = input()

new = ''
for c in s:
    # if ("0" <= c <= "9" or
    #         "a" <= c <= "z" or
    #         "A" <= c <= "Z" or c == " "):
    if c.isalnum() or c == " ":
        new += c

# if "0"<=c<="9"or"a"<=c<="z"

# print(new)

listOfWords = new.split()
print(len(listOfWords))
