from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from time import strftime
import requests
import psutil


def on_leave(event):
    msg.configure(bg='black')


def on_motion(event):
    msg.configure(bg='cyan')


def x(event):
    p = messagebox.askyesno('Exit', 'Do you want to exit ?')
    if p == 1:
        master.destroy()


def on_double_click(event):
    e = LabelFrame(master, bg='blue', width=250, height=250)
    e.place(x=0, y=25)
    e0 = Label(e, image=p1, width=100, height=100, bg='black')
    e0.grid(row=0, column=0, columnspan=3)

    def o0():
        e.destroy()

    def move(event):
        component = event.widget
        locx, locy = component.winfo_x(), component.winfo_y()
        w, h = master.winfo_width(), master.winfo_height()
        mx, my = component.winfo_width(), component.winfo_height()
        xpos = (locx + event.x) - (15)
        ypos = (locy + event.y) - int(my / 2)
        if xpos >= 0 and ypos >= 0 and w - abs(xpos) >= 0 and h - abs(ypos) >= 0 and xpos <= w - 5 and ypos <= h - 5:
            component.place(x=xpos, y=ypos)

    def o2():
        e.place(x=500, y=500)
        t1 = Label(task, image=p1)
        t1.place(x=0, y=0)

        def t2(event):
            t1.destroy()
            e.place(x=0, y=25)

        t1.bind('<Button-1>', t2)

    o = Button(e, text='X', command=o0, bg='cyan')
    o.grid(row=1, column=0)
    o1 = Button(e, text='-', command=o2, bg='cyan')
    o1.grid(row=1, column=1)
    e.bind('<B1-Motion>', move)


def left_click(event):
    msg.destroy()
    p0.grid(row=wo, column=we)


master = Tk()
master.iconbitmap('')
master.title('Desktop')
master.resizable(False, False)
master.geometry('250x250')
master.configure(bg='black')
master.bind('<x>', x)
task = LabelFrame(master, bg='blue', width=250, height=5)
task.place(x=0, y=224)
t2 = Label(task, text='', bg='blue', width=34, height=1)
t2.grid(row=0, column=0)
t3 = Label(master, text='', bg='black', fg='white', font=('calibri', 10, 'bold'))
t3.place(x=165, y=0)
e10 = Label(master, text='', bg='black', fg='white', font=('calibri', 10, 'bold'))
e10.place(x=106, y=0)


def time():
    global t3
    string = strftime('%I:%M:%S %p')
    t3.configure(text=string)
    t3.after(1000, time)


time()


def p2():
    try:
        global msg, p1
        p0.grid_forget()
        p3 = filedialog.askopenfilename(initialdir='', title='Select a File')
        p1 = PhotoImage(file=p3)
        msg = Label(master, image=p1, bg='black', width=20, height=20)
        msg.bind('<Leave>', on_leave)
        msg.bind('<Motion>', on_motion)
        msg.bind('<Double-Button-1>', on_double_click)
        msg.bind('<Button-3>', left_click)
        msg.grid(row=wo, column=we)
    except Exception:
        p2()


try:
    def ce9():
        global e9
        url = "http://www.google.com"
        timeout = 5

        try:
            request = requests.get(url, timeout=timeout)
            e8 = PhotoImage(file='connected.png')
            e9.configure(image=e8)
            e9.update()
            try:
                ce9()
            except Exception:
                pass

        except (requests.ConnectionError, requests.Timeout):
            e8 = PhotoImage(file='notconnected.png')
            e9.configure(image=e8)
            e9.update()
            try:
                ce9()
            except Exception:
                pass


except Exception:
    pass


def e12():
    global e10
    bttery = psutil.sensors_battery()
    e10.configure(text='  |  ' + str(bttery.percent) + '%  | ')
    e10.after(1000, e12)


e12()
we = 0
wo = 0
p0 = Button(master, text='+', bg='black', fg='white', font=('calibri', 10, 'bold'), command=p2)
p0.grid(row=wo, column=we)
e9 = Label(master, bg='black', fg='white')
e9.place(x=86, y=0)
ce9()
master.mainloop()