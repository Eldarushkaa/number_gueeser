from tkinter import *
import numpy as np
import main


main

A = np.zeros((28, 28))
t = 0
H = []


def paint(event):
    global t, H
    if 20 <= event.x < 540 and 0 <= event.y < 540:
        c.create_oval(event.x - 30, event.y - 30, event.x + 30, event.y + 30, fill='black')
        A[event.y // 20][event.x // 20 + 1] = 1
        A[event.y // 20][event.x // 20 - 1] = 1
        A[event.y // 20][event.x // 20] = 1
        A[event.y // 20 - 1][event.x // 20] = 1
        A[event.y // 20 + 1][event.x // 20] = 1
        if t == 10:
            H = main.model_answer(main.model, A)[0]
            for i in range(10):
                B[i].configure(bg='#' + str('%02x%02x%02x' % (255 - int(255 * H[i]), 255, 255 - int(255 * H[i]))))
            t = 0
        else:
            t += 1


def clear():
    global A
    A = np.zeros((28, 28))
    c.delete('all')
    for i in range(10):
        B[i].configure(bg='white')


root = Tk()
root.resizable(width=False, height=False)
root.geometry('564x590+100+100')

c = Canvas(width=560, height=560, bg='white')
c.grid(row=1, columnspan=11)

root.bind('<B1-Motion>', paint)

clear_btn = Button(root, text="Clear all", width=10, command=clear)
clear_btn.grid(row=0, column=0, sticky=W)


B = [Button(root, text=str(i), width=5, bg='white') for i in range(10)]
for i in range(10):
    B[i].grid(row=0, column=1+i, sticky=W)


if __name__ == '__main__':

    root.mainloop()
