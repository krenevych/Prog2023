# Дано текстовий файл, що містить послідовність слів.
# Крім цього задано пару слів w1 та w2.
# Замінити у файлі усі входження слова w1, словом w2.

f_in = open("input10.txt")
content = f_in.read()
f_in.close()
print(content)
w_what_change = "hello"
w_to_change = "bye"
new_content = content.replace(w_what_change, w_to_change)

f_out = open("input10.txt", "w")
print(new_content, file=f_out)
f_out.close()

