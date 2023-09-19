# Задається номер місяця, необхідно визначити до якого сезону він належить

month = 33

if month == 12 or 1 <= month <= 2:
    print("Зима")
elif 3 <= month <= 5:
    print("Весна")
elif 6 <= month <= 8:
    print("Літо")
elif 9 <= month <= 11:
    print("Осінь")
else:
    print("місяць заданий неправильно")

pass
