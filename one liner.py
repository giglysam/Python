from tkinter import *
root = Tk()
root.resizable(False, False)
ope = ["+", "-", "x", ":"]

l = Label(root, text='Calculator', font=('calibri', 15, 'bold'), fg='red')
l.grid(row=0, column=0)

p = Label(root, font=('calibri', 10, 'bold'))
p.grid(row=2, column=0)

inp = Entry(root, font=('calibri', 10, 'bold'))
inp.grid(row=1, column=0)


def o(event):
    for i in inp.get():
        try:
            if i in ope:
                a, b = str(inp.get()).split(i)

                if i == "+":
                    p.configure(text=str(int(a) + int(b)))
                elif i == "-":
                    p.configure(text=str(int(a) - int(b)))
                elif i == "x":
                    p.configure(text=str(int(a) * int(b)))
                elif i == ":":
                    p.configure(text=str(int(a) / int(b)))
        except Exception:
            pass


root.bind('<Return>', o)
root.mainloop()