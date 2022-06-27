from tkinter import *
import random
root = Tk()
root.resizable(False, False)
root.geometry('120x70')
a = ['red', 'blue', 'green', 'yellow', 'black']
s = 0


def g():
    global root, s, a
    a0 = Label(root, width=4, height=2, bg=random.choice(a))
    a0.place(x=0, y=0)
    a1 = Label(root, width=4, height=2, bg=random.choice(a))
    a1.place(x=33, y=0)
    a2 = Label(root, width=4, height=2, bg=random.choice(a))
    a2.place(x=0, y=33)
    a3 = Label(root, width=4, height=2, bg=random.choice(a))
    a3.place(x=33, y=33)

    a4 = Label(root, text=s, font=('calibri', 15, 'bold'))
    a4.place(x=85, y=20)

    def b0(event):
        global s
        if a0.cget('bg') == a1.cget('bg'):
            a0.configure(bg=random.choice(a))
            a0.update()
            a1.configure(bg=random.choice(a))
            a1.update()
            s += 2
            a4.configure(text=s)
            a4.update()

    def b1(event):
        global s
        if a0.cget('bg') == a2.cget('bg'):
            a0.configure(bg=random.choice(a))
            a0.update()
            a2.configure(bg=random.choice(a))
            a2.update()
            s += 2
            a4.configure(text=s)
            a4.update()

    def b2(event):
        global s
        if a1.cget('bg') == a3.cget('bg'):
            a1.configure(bg=random.choice(a))
            a1.update()
            a3.configure(bg=random.choice(a))
            a3.update()
            s += 2
            a4.configure(text=s)
            a4.update()

    def b3(event):
        global s
        if a2.cget('bg') == a3.cget('bg'):
            a2.configure(bg=random.choice(a))
            a2.update()
            a3.configure(bg=random.choice(a))
            a3.update()
            s += 2
            a4.configure(text=s)
            a4.update()

    def b4(event):
        global s
        s -= 1
        a0.configure(bg=random.choice(a))
        a1.configure(bg=random.choice(a))
        a2.configure(bg=random.choice(a))
        a3.configure(bg=random.choice(a))

    a0, a1.bind('<B1-Motion>', b0)
    a0, a2.bind('<B1-Motion>', b1)
    a1, a0.bind('<B1-Motion>', b0)
    a2, a0.bind('<B1-Motion>', b1)
    a1, a3.bind('<B1-Motion>', b2)
    a3, a2.bind('<B1-Motion>', b3)
    a3, a1.bind('<B1-Motion>', b2)
    a2, a3.bind('<B1-Motion>', b3)
    root.bind('<Return>', b4)
    root.mainloop()


g()
