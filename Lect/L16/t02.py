my_file = open("input.txt", "rt")

print("Read 1")
for line in my_file:
    print(line, end="")
# my_file.close()
#
# my_file = open("input.txt", "rt")
# my_file.seek(0)
print("\nRead 2")
for line in my_file:
    print(line, end="")

my_file.close()
