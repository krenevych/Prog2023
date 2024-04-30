from tkinter import *

root = Tk()
# Створюємо полотно
canvas = Canvas(root, width=400, height=300)
canvas.pack(side=LEFT)
# Створюємо овал
id = canvas.create_oval(20, 20, 40, 40)


def onCanvasClick(ev):
        move(id)


def move(ids): # Переміщуємо елемент на 5 пікселів по осі X
    canvas.move(ids, 5, 0)  # Рекурсивно викликаємо функцію move через 25 мілісекунд    # та передаємо їй параметр ids
    canvas.after(100, move, ids)

canvas.bind('<Button-1>', onCanvasClick)

if __name__ == '__main__':
    root.mainloop()
