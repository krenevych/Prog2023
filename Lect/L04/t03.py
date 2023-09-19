# Задається номер місяця, необхідно визначити до якого сезону він належить

month = 3

if month == 12 or 1 <= month <= 2:
    print("Зима")
else:
    if 3 <= month <= 5:
        print("Весна")
    else:
        if 6 <= month <= 8:
            print("Літо")
        else:
            if 9 <= month <= 11:
                print("Осінь")
            else:
                print("місяць заданий неправильно")

pass