f = open("input.txt")
ktest = int(f.readline())
for i in range(ktest):
    knumb = int(f.readline())
    dnumb = {}
    for j in range(knumb):
        curr = int(f.readline())
        if curr in dnumb:
            dnumb[curr] += 1
        else:
            dnumb[curr] = 1
    # print(dnumb)
    m = max(dnumb.values())
    list_max = []
    for k, v in dnumb.items():
        if v == m:
            list_max.append(k)
    # print("list_max", min(list_max))
    print(min(list_max))

f.close()
