import os


for path in os.walk("."):
    for file in path[2]:
        print(file)
        with open(file) as f:
            print(f.read())
