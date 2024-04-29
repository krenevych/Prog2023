from tkinter import *

main_window = Tk()  # створюємо головне вікно програми

def callback():
    print("Hello!")
    btn["text"] = "Hello!"


btn = Button(main_window,  # контейнер, що містить
             text="Click me",  # надпис на кнопці
             width=20, height=5,  # ширина та висота
             bg="white", fg="black",  # колір фону і напису
             font="Arial 18",  # шрифт надпису та розмір
             command=callback)  # функція обробки подій
btn.pack()


if __name__ == '__main__':
    main_window.mainloop()  # запускаємо цикл головного вікна
