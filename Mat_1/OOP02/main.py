from EqReader import EqReader

reader = EqReader("input.txt")
eqs = reader.read()
for eq in eqs:
    eq.show()