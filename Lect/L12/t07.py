# print(max(1, 4, 5, 6, 7, 6))
def max(*args):
    if len(args) == 0:
        return None
    m = args[0]
    for el in args[1:]:
        if el > m:
            m = el
    return m


print(max())