def inc(c: str):
    d = str((int(c) + 1) % 10)
    return d

def consist(c, setOfChars):
    return c in setOfChars

def solve(s, setOfCharsToRemove, digetsToIcrease):
    new = ""
    for c in s:
        if consist(c, setOfCharsToRemove):
            continue

        # if c in "02468":
        if consist(c, digetsToIcrease):
            # new += chr(ord(c)+1)
            new += inc(c)
        else:
            new += c
        return new


s = input() # s = "abddb3459"
print(solve(s, "acd", "24"))
