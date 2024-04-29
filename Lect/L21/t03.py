from tkinter import *

main_window = Tk()  # створюємо головне вікно програми

def sayHello():
    print("Hello!")



btn = Button(main_window,  # контейнер, що містить
             text="Click me",  # надпис на кнопці
             width=20, height=5,  # ширина та висота
             bg="white", fg="black",  # колір фону і напису
             font="Arial 18",  # шрифт надпису та розмір
             )  #

def moveMouseOverBtn(even):
    print(even)

btn.pack()
# btn.bind("<Button-1>", sayHello, )
# btn.bind("<Button-2>", sayHello)
# btn.bind("<Button3>", sayHello)
btn.bind("<Motion>", moveMouseOverBtn)


def callback(event):
    print("Control-Alt-q pressed")
    print(event)

main_window.bind("<Control-Alt-q>", callback)



if __name__ == '__main__':
    main_window.mainloop()  # запускаємо цикл головного вікна
