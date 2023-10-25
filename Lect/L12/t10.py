def func():
    global x
    x += 44  # не локальна змінна, бо ми позначили її як global
    # print(x)


x = 1  # глобальна змінна
func()
func()
func()
func()
print(x)
