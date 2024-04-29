from tkinter import *
from tkinter.filedialog import askopenfilename

main_window = Tk()  # створюємо головне вікно програми

def sayHello():
    print("Hello!")



def readFile():
    filename = askopenfilename()
    with open(filename) as f:
        for line in f:
            print(line)

btn = Button(main_window,  # контейнер, що містить
             text="Click me",  # надпис на кнопці
             width=20, height=5,  # ширина та висота
             bg="white", fg="black",  # колір фону і напису
             font="Arial 18",  # шрифт надпису та розмір
             command=readFile)  #

btn.pack()



if __name__ == '__main__':
    main_window.mainloop()  # запускаємо цикл головного вікна
