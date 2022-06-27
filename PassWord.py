from tkinter import *
root = Tk()
root.title('PassWord')
root.resizable(False, False)
t = Entry(root, show='●', font=('calibri', 15, 'bold'), relief=FLAT)
t.grid(row=0, column=0)


def d(event):
    t.configure(show='', font=('calibri', 15, 'bold'), relief=FLAT)

    def b(event):
        t.configure(show='●', font=('calibri', 15, 'bold'), relief=FLAT)
        r.configure(text='-__-')
        r.bind('<Button-1>', d)

    r.configure(text='o_o')
    r.bind('<Button-1>', b)


r = Label(root, text='-__-', font=('calibri', 15, 'bold'))
r.grid(row=0, column=2)
r.bind('<Button-1>', d)
root.mainloop()
