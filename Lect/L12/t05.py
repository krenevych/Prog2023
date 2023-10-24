def inc(lst: list):
    # lst = myLst
    lst.append(1)
    print(lst)


######## main #########
myLst = [1, 2]
inc(myLst.copy())
print(myLst)