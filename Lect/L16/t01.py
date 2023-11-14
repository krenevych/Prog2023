my_file = open("out.txt", "r+t")

# s = "Hello, world"
# print(s)  # виводимо на екран
s = "New"
print(s, file=my_file)  # записуємо у файл my_file

my_file.close()
