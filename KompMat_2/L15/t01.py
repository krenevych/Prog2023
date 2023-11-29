def read():
    f = open("input.txt")
    deg1 = int(f.readline())
    first = {}
    for i in range(deg1):
        deg, coef = map(int, f.readline().split())
        first[deg] = coef
    deg2 = int(f.readline())
    second = {}
    for i in range(deg2):
        deg, coef = map(int, f.readline().split())
        second[deg] = coef


def mult(P: dict, Q: dict):
    R = {}
    for dp, cp in P.items():
        for dq, cq in Q.items():
            d = dp + dq
            c = cp * cq
            # print(d, c)
            if d in R:
                R[d] += c
            else:
                R[d] = c
    return R

def writePolinom(P: dict):
    degs = list(P.keys())
    degs.sort()
    degs.reverse()
    # print(d)
    for d in degs:
        print(f"{P[d]}xˆ{d}+", end="")

f, s = read()
r = mult(f, s)
print(r)
writePolinom(r)
# print(s)
