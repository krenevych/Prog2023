# Дано текстовий файл, що містить принаймні один непорожній рядок. Описати підпрограми:
# a)	виведення усіх рядків файла;
# b)	виведення рядків, які містять більше
#       60 символів;
# c)	підрахунку кількості порожніх рядків;
# d)	пошуку найдовшого рядка;

with open("input01.txt") as myFile:
    content = myFile.read()
    print(content)

    myFile.seek(0)
    for line in myFile:
        stripped = line.rstrip()
        print(stripped)

