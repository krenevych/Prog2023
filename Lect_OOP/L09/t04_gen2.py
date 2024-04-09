def SN():  # нескінченний генератор
    S = 1
    n = 1
    yield S
    while True:
        n += 1
        S = 2 * S + n ** 2
        yield S

    # return <-> StopIteration


A = int(input("A = "))
i = 1
for s in SN():
    print(f"S({i})={s}")
    i += 1
    if s > A:
        break # у змінній s міститься перший член нашої послідовності, що більший за введене з клавіатури число A
