from tkinter import *
root = Tk()
root.title("CALCULATOR")
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def cv(number):
    c = e.get()
    e.delete(0, END)
    e.insert(0, str(c) + str(number))


def co():
    e.delete(0, END)


def cp():
    fn = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(fn)
    e.delete(0, END)


def cb():
       sn = e.get()
       e.delete(0, END)
       if math == "addition":
         e.insert(0, f_num + int(sn))
       elif math == "substraction":
         e.insert(0, f_num - int(sn))
       elif math == "multiplication":
         e.insert(0, f_num * int(sn))
       elif math == "division":
         e.insert(0, f_num / int(sn))


def ck():
    fn = e.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(fn)
    e.delete(0, END)


def cn():
    fn = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(fn)
    e.delete(0, END)


def cx():
    fn = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(fn)
    e.delete(0, END)


b1 = Button(root, text="1", padx=40, pady=20, command=lambda: cv(1))
b2 = Button(root, text="2", padx=40, pady=20, command=lambda: cv(2))
b3 = Button(root, text="3", padx=40, pady=20, command=lambda: cv(3))
b4 = Button(root, text="4", padx=40, pady=20, command=lambda: cv(4))
b5 = Button(root, text="5", padx=40, pady=20, command=lambda: cv(5))
b6 = Button(root, text="6", padx=40, pady=20, command=lambda: cv(6))
b7 = Button(root, text="7", padx=40, pady=20, command=lambda: cv(7))
b8 = Button(root, text="8", padx=40, pady=20, command=lambda: cv(8))
b9 = Button(root, text="9", padx=40, pady=20, command=lambda: cv(9))
b0 = Button(root, text="0", padx=40, pady=20, command=lambda: cv(0))
ba = Button(root, text="+", padx=39, pady=20, command=lambda: cp())
bo = Button(root, text="=", padx=39, pady=20, command=lambda: cb())
bk = Button(root, text="clear", padx=30, pady=20, command=lambda: co())
bg = Button(root, text="_", padx=39, pady=20, command=lambda: ck())
bv = Button(root, text="x", padx=39, pady=20, command=lambda: cn())
bx = Button(root, text=":", padx=39, pady=20, command=lambda: cx())
B5 = Button(root, text="error", relief=RAISED, bitmap="error", state=DISABLED)
B9 = Button(root, text="hourglass", relief=RAISED, bitmap="hourglass", state=DISABLED)

b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=3, column=0)
b8.grid(row=3, column=1)
b9.grid(row=3, column=2)

b0.grid(row=4, column=0)
ba.grid(row=4, column=1)
bo.grid(row=6, column=0)
bk.grid(row=4, column=2)

bg.grid(row=5, column=0)
bv.grid(row=5, column=1)
bx.grid(row=5, column=2)
B5.grid(row=6, column=2)
B9.grid(row=6, column=1)
root.mainloop()