def printStrWith1Space(st):
    words = st.split()
    st = " ".join(words)
    print(st)


st = "   pentium    core    i7   "
result = printStrWith1Space(st)
print(result)