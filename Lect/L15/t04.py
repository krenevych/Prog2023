my_file = open("myfile.rrr", "rt")
# print(my_file)
lines = []
for line in my_file:
    # line = line[:-1]
    # line = line.rstrip()
    lines.append(line)
    print(line)
my_file.close()

print(lines)