d = {
    "Hello": "World",
    3: "3",
    "3": 3,
}

if "Hello" in d:
    print(d["Hello"])
else:
    print(None)

print(d.get("66666"))
print(d.get("66666", "Default value"))