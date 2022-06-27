from tkinter import *
import random
root = Tk()
root.title('TNT')
root.resizable(False, False)
root.configure(bg='white')
a = Label(root, bg='black', width=4, height=2)
a.place(x=150, y=5)
a0 = Label(root, bg='black', width=4, height=2)
a0.place(x=150, y=45)
a1 = Label(root, bg='black', width=4, height=2)
a1.place(x=150, y=85)
a2 = Label(root, bg='black', width=4, height=2)
a2.place(x=150, y=125)
a4 = Label(root, bg='black', width=4, height=1)
a4.place(x=150, y=165)
a3 = Label(root, bg='blue', width=2, height=1)
a3.place(x=70, y=80)
p = 0


def b(event):
    global p
    o = ['72', '80', '75', '66', '69', '79', '62', '89', '86', '83']
    o0 = random.choice(o)
    o1 = random.choice(o)
    a3.place(x=o0, y=o1)
    a3.configure(bg='blue')

    a.configure(bg='red')
    a.bind('<Leave>', c)
    a0.bind('<Leave>', c)
    a1.bind('<Leave>', c)
    a2.bind('<Leave>', c)


def b0(event):
    global p
    o = ['62', '70', '65', '56', '59', '89', '72', '99', '96', '93']
    o0 = random.choice(o)
    o1 = random.choice(o)
    a3.place(x=o0, y=o1)
    a3.configure(bg='green')

    a.configure(bg='red')
    a0.configure(bg='red')
    a.bind('<Leave>', c)
    a0.bind('<Leave>', c)
    a1.bind('<Leave>', c)
    a2.bind('<Leave>', c)


def b1(event):
    global p
    o = ['52', '60', '55', '46', '49', '99', '82', '109', '106', '103']
    o0 = random.choice(o)
    o1 = random.choice(o)
    a3.place(x=o0, y=o1)
    a3.configure(bg='yellow')

    a.configure(bg='red')
    a0.configure(bg='red')
    a1.configure(bg='red')
    a.bind('<Leave>', c)
    a0.bind('<Leave>', c)
    a1.bind('<Leave>', c)
    a2.bind('<Leave>', c)


def b2(event):
    global p
    o = ['42', '50', '45', '36', '39', '109', '92', '119', '116', '103']
    o0 = random.choice(o)
    o1 = random.choice(o)
    a3.place(x=o0, y=o1)
    a3.configure(bg='orange')
    a.configure(bg='red')
    a0.configure(bg='red')
    a1.configure(bg='red')
    a2.configure(bg='red')

    a.bind('<Leave>', c)
    a0.bind('<Leave>', c)
    a1.bind('<Leave>', c)
    a2.bind('<Leave>', c)


def b3(event):
    global p
    o = ['32', '40', '35', '26', '29', '119', '102', '129', '126', '113']
    o0 = random.choice(o)
    o1 = random.choice(o)
    a3.place(x=o0, y=o1)
    a3.configure(bg='red')

    a.configure(bg='red')
    a0.configure(bg='red')
    a1.configure(bg='red')
    a2.configure(bg='red')
    a4.configure(bg='red')

    a.bind('<Leave>', c)
    a0.bind('<Leave>', c)
    a1.bind('<Leave>', c)
    a2.bind('<Leave>', c)
    a3.bind('<Leave>', c)
    a4.bind('<Leave>', c)


def c(event):
    a3.place(x=70, y=80)
    a.configure(bg='black')
    a0.configure(bg='black')
    a1.configure(bg='black')
    a2.configure(bg='black')
    a3.configure(bg='blue')
    a4.configure(bg='black')


a.bind('<Motion>', b)
a0.bind('<Motion>', b0)
a1.bind('<Motion>', b1)
a2.bind('<Motion>', b2)
a4.bind('<Motion>', b3)
root.mainloop()
