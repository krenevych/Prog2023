from t04 import Dictionary4

d = Dictionary4()
d["1234"] = 1234
d["zxcv"] = 12
print(d)
print("1234" in d)
print("34543" not in d)
del d["1234"]
print(d)

