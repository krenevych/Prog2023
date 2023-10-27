def sym(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and sym(s[1:-1])

print(sym("aabbccbbaIa"))