from tkinter import *
import datetime
root = Tk()
root.title('Birth')
root.resizable(False, False)
year = datetime.date.today().year
a = Label(root, text='Enter age : ', bg='white')
a.grid(row=0, column=0)
a0 = Entry(root, relief=FLAT, width=22)
a0.grid(row=0, column=1)


def a1(event):
    try:
        re = float(year) - float(a0.get())
        MessageBox.showinfo('Birth Year', 'Your Born in ' + str(re))
        a0.delete(0, END)
    except Exception:
        pass


root.bind('<Return>', a1)
root.mainloop()