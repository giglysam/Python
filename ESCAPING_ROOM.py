from tkinter import *
from tkinter import messagebox


root = Tk()
root.resizable(False, False)
root.title('ESCAPING ROOM')
a = PhotoImage(file='room.png')
b = PhotoImage(file='door.png')
a0 = Label(root, image=a)
a0.grid(row=0, column=0)
a1 = Entry(root, width=4)
a1.place(x=412, y=248)


def a2(event):
    if a1.get() == '0956':
        a1.destroy()
        a3 = Label(root, text='8888')
        a3.place(x=412, y=248)
        a4 = Entry(root, width=4)
        a4.place(x=225, y=280)

        def a5(event):
            if a4.get() == '8888':
                a4.destroy()
                a7 = Label(root, text='🔑', fg='gray49')
                a7.place(x=225, y=281)

                def a6(event):

                    def c():
                        global a9, b9
                        messagebox.showinfo('BRAVO', 'YOU COMPLETED THE ESCAPING ROOM')
                        a0.destroy()
                        a3.destroy()
                        a7.destroy()
                        g.destroy()

                        a9 = PhotoImage(file='room1.png')
                        b9 = PhotoImage(file='door.png')
                        a09 = Label(root, image=a9)
                        a09.grid(row=0, column=0)
                        a19 = Entry(root, width=3, bg='gray')
                        a19.place(x=230, y=230)

                        def a29(event):
                            if a19.get() == '2167':
                                a19.destroy()
                                a79 = Label(root, text='🔑', fg='white', bg='gray')
                                a79.place(x=240, y=238)

                                def a69(event):

                                    def c9():
                                        messagebox.showinfo('BRAVO', 'YOU COMPLETED THE ESCAPING ROOM')

                                    g9 = Button(root, image=b9, command=c9)
                                    g9.place(x=41, y=96)

                                a79.bind('<Button-1>', a69)
                            else:
                                messagebox.showinfo('False', 'WRONG INPUT')

                        a19.bind('<Return>', a29)

                    g = Button(root, image=b, command=c)
                    g.place(x=33, y=99)

                a7.bind('<Button-1>', a6)
            else:
                messagebox.showinfo('False', 'WRONG INPUT')

        a4.bind('<Return>', a5)

    else:
        messagebox.showinfo('False', 'WRONG INPUT')


a1.bind('<Return>', a2)
root.mainloop()