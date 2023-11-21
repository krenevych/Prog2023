x = 0

try:
    if x == 0:
        raise ZeroDivisionError
    else:
        print(1 / x)
except ZeroDivisionError:
    print('Ділення на нуль')
