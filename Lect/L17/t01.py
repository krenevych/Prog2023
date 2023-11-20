# припустимо я хочу рахувати 12 / n

try:
    f = open("qqqq.txt")
    n = int(f.readline())
    k = 12 / n
    print(k)
    print("Програма завершилася природнім чином")
    f.close()
except ZeroDivisionError:
    print("Ділити на нуль дуже погана прикмета для математика!")
except FileNotFoundError:
    print("Файл відсутній!")
except ValueError:
    print("Не змогли конвертувати вміст файла у int")
else:
    print("Цей блок коду виконується лише, якщо в блоці try не виникло виключної ситуації")
finally:
    print("Цей блок коду виконується завжди")

pass


