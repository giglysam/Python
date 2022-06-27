from tkinter import *


def IT():
    root = Tk()
    root.title('dinosaur')
    root.resizable(False, False)
    a = Label(root, text='🦕', font=('calibri', 25, 'bold'), fg='gray')
    a.place(x=20, y=150)

    d = Label(root, text='🦖', font=('calibri', 25, 'bold'), fg='brown')
    d.place(x=70, y=150)

    e = Label(root, text='🐉', font=('calibri', 25, 'bold'), fg='red')
    e.place(x=120, y=150)

    b = Label(root, fg='lime', font=('calibri', 30, 'bold'))
    b.place(x=30, y=20)

    b1 = Label(root, text='  ', bg='lime', font=('calibri', 20, 'bold'))
    b1.place(x=50, y=30)

    b2 = Label(root, text='  ', bg='lime', font=('calibri', 20, 'bold'))
    b2.place(x=50, y=40)

    b3 = Label(root, text='  ', bg='lime', font=('calibri', 20, 'bold'))
    b3.place(x=50, y=50)

    b4 = Label(root, text='  ', bg='lime', font=('calibri', 20, 'bold'))
    b4.place(x=50, y=60)

    b5 = Label(root, text='  ', bg='lime', font=('calibri', 20, 'bold'))
    b5.place(x=40, y=30)

    b6 = Label(root, text='  ', bg='lime', font=('calibri', 20, 'bold'))
    b6.place(x=40, y=40)

    b7 = Label(root, text='  ', bg='lime', font=('calibri', 20, 'bold'))
    b7.place(x=40, y=50)

    b8 = Label(root, text=' ', bg='lime', font=('calibri', 20, 'bold'))
    b8.place(x=40, y=60)

    b9 = Label(root, text=' ', bg='lime', font=('calibri', 20, 'bold'))
    b9.place(x=60, y=30)

    b10 = Label(root, text=' ', bg='lime', font=('calibri', 20, 'bold'))
    b10.place(x=60, y=40)

    b11 = Label(root, text=' ', bg='lime', font=('calibri', 20, 'bold'))
    b11.place(x=60, y=50)

    b12 = Label(root, text=' ', bg='lime', font=('calibri', 20, 'bold'))
    b12.place(x=60, y=60)

    b13 = Label(root, text=' ', bg='lime', font=('calibri', 20, 'bold'))
    b13.place(x=70, y=50)

    b14 = Label(root, text=' ', bg='lime', font=('calibri', 20, 'bold'))
    b14.place(x=80, y=50)

    b15 = Label(root, text=' ', bg='lime', font=('calibri', 20, 'bold'))
    b15.place(x=30, y=50)

    b16 = Label(root, text=' ', bg='lime', font=('calibri', 20, 'bold'))
    b16.place(x=20, y=50)

    b17 = Label(root, text=' ', bg='brown', font=('calibri', 25, 'bold'))
    b17.place(x=50, y=70)

    def c1(event):
        b1.destroy()

    def c2(event):
        b2.destroy()

    def c3(event):
        b3.destroy()

    def c4(event):
        b4.destroy()

    def c5(event):
        b5.destroy()

    def c6(event):
        b6.destroy()

    def c7(event):
        b7.destroy()

    def c8(event):
        b8.destroy()

    def c9(event):
        b9.destroy()

    def c10(event):
        b10.destroy()

    def c11(event):
        b11.destroy()

    def c12(event):
        b12.destroy()

    def c13(event):
        b13.destroy()

    def c14(event):
        b14.destroy()

    def c15(event):
        b15.destroy()

    def c16(event):
        b16.destroy()

    def a0(event):
        root.configure(cursor='spraycan')
        b.configure(text=str(a.cget('text')), fg='gray')
        b1.bind('<B1-Motion>', c1)
        b2.bind('<B1-Motion>', c2)
        b3.bind('<B1-Motion>', c3)
        b4.bind('<B1-Motion>', c4)
        b5.bind('<B1-Motion>', c5)
        b6.bind('<B1-Motion>', c6)
        b7.bind('<B1-Motion>', c7)
        b8.bind('<B1-Motion>', c8)
        b9.bind('<B1-Motion>', c9)
        b10.bind('<B1-Motion>', c10)
        b11.bind('<B1-Motion>', c11)
        b12.bind('<B1-Motion>', c12)
        b13.bind('<B1-Motion>', c13)
        b14.bind('<B1-Motion>', c14)
        b15.bind('<B1-Motion>', c15)
        b16.bind('<B1-Motion>', c16)
        a.destroy()
        d.destroy()
        e.destroy()

    def d0(event):
        root.configure(cursor='spraycan')
        b.configure(text=str(d.cget('text')), fg='brown')
        b1.bind('<B1-Motion>', c1)
        b2.bind('<B1-Motion>', c2)
        b3.bind('<B1-Motion>', c3)
        b4.bind('<B1-Motion>', c4)
        b5.bind('<B1-Motion>', c5)
        b6.bind('<B1-Motion>', c6)
        b7.bind('<B1-Motion>', c7)
        b8.bind('<B1-Motion>', c8)
        b9.bind('<B1-Motion>', c9)
        b10.bind('<B1-Motion>', c10)
        b11.bind('<B1-Motion>', c11)
        b12.bind('<B1-Motion>', c12)
        b13.bind('<B1-Motion>', c13)
        b14.bind('<B1-Motion>', c14)
        b15.bind('<B1-Motion>', c15)
        b16.bind('<B1-Motion>', c16)
        a.destroy()
        d.destroy()
        e.destroy()

    def e0(event):
        root.configure(cursor='spraycan')
        b.configure(text=str(e.cget('text')), fg='red')
        b1.bind('<B1-Motion>', c1)
        b2.bind('<B1-Motion>', c2)
        b3.bind('<B1-Motion>', c3)
        b4.bind('<B1-Motion>', c4)
        b5.bind('<B1-Motion>', c5)
        b6.bind('<B1-Motion>', c6)
        b7.bind('<B1-Motion>', c7)
        b8.bind('<B1-Motion>', c8)
        b9.bind('<B1-Motion>', c9)
        b10.bind('<B1-Motion>', c10)
        b11.bind('<B1-Motion>', c11)
        b12.bind('<B1-Motion>', c12)
        b13.bind('<B1-Motion>', c13)
        b14.bind('<B1-Motion>', c14)
        b15.bind('<B1-Motion>', c15)
        b16.bind('<B1-Motion>', c16)
        a.destroy()
        d.destroy()
        e.destroy()

    def IT0(event):
        root.destroy()
        IT()

    a.bind('<Button-1>', a0)
    d.bind('<Button-1>', d0)
    e.bind('<Button-1>', e0)
    root.bind('<Return>', IT0)
    root.mainloop()


IT()