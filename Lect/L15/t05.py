my_file = open("out.txt", "wt")

s = "Hello, world"
# print(s)  # виводимо на екран
print(s, file=my_file)  # записуємо у файл my_file

my_file.close()
