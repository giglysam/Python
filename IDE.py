import os
from tkinter import *
root = Tk()
e = Text(root)
e.pack()


def e0(event):
    s = open('code.py', 'a')
    s.write(str(e.get(1.0, END)))
    s.close()
    import code


def e1(event):
        os.remove('code.py')


root.bind('<Alt-d>', e1)
e.bind('<Alt-r>', e0)
root.mainloop()


