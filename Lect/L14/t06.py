d = {
    "Hello": "World",
    3: "3",
    "3": 3,
}
print(d)
d["34"] = 34
print(d)
d["Hello"] = 34
print(d)

if "666666" in d:
    print(d["666666"])
else:
    print(None)

if "Hello" in d:
    print(d["Hello"])
else:
    print(None)
