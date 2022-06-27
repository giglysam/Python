from Tkinter import *
import webbrowser
root = Tk()
root.title('')
root.resizable(False, False)
a = Label(root, text='WEBBROWSER', font=('calibri', 15, 'bold'), fg='blue')
a.grid(row=0, column=0)
a0 = Entry(root, font=('calibri', 10, 'bold'))
a0.grid(row=1, column=0)


def a1(event):
    global a0
    url = "https://www.google.com.tr/search?q={}".format(a0.get())
    webbrowser.open(url)


root.bind('<Return>', a1)
root.mainloop()