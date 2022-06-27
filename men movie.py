import time
from tkinter import *


root = Tk()
root.title('')
root.resizable(False, False)

root.withdraw()
s = 0
o = PhotoImage(file='popets/y0.png')
o1 = PhotoImage(file='popets/y1.png')
o2 = PhotoImage(file='popets/y2.png')
o3 = PhotoImage(file='popets/y3.png')
o4 = PhotoImage(file='popets/y4.png')
o5 = PhotoImage(file='popets/y5.png')
o6 = PhotoImage(file='popets/y6.png')
o7 = PhotoImage(file='popets/y7.png')
o8 = PhotoImage(file='popets/y8.png')
o9 = PhotoImage(file='popets/y9.png')
o10 = PhotoImage(file='popets/y10.png')
o11 = PhotoImage(file='popets/y11.png')
o12 = PhotoImage(file='popets/y12.png')
o13 = PhotoImage(file='popets/y13.png')
o14 = PhotoImage(file='popets/y14.png')
o15 = PhotoImage(file='popets/y15.png')
o16 = PhotoImage(file='popets/y16.png')
o0 = Label(root)
o0.grid(row=0, column=0)

def l():
        try:
            global s, o0
            root.deiconify()
            o0.configure(image=o)
            o0.update()
            time.sleep(0.2)
            s += 1

            if s == 1:
                o0.configure(image=o1)
                o0.update()
                time.sleep(0.2)
                s += 1
                if s == 2:
                    o0.configure(image=o2)
                    o0.update()
                    time.sleep(0.2)
                    s += 1
                    if s == 3:
                        o0.configure(image=o3)
                        o0.update()
                        time.sleep(0.2)
                        s += 1
                        if s == 4:
                            o0.configure(image=o4)
                            o0.update()
                            time.sleep(0.2)
                            s += 1
                            if s == 5:
                                o0.configure(image=o5)
                                o0.update()
                                time.sleep(0.2)
                                s += 1
                                if s == 6:
                                    o0.configure(image=o6)
                                    o0.update()
                                    time.sleep(0.2)
                                    s += 1
                                    if s == 7:
                                        o0.configure(image=o7)
                                        o0.update()
                                        time.sleep(0.2)
                                        s += 1
                                        if s == 8:
                                            o0.configure(image=o8)
                                            o0.update()
                                            time.sleep(0.2)
                                            s += 1
                                            if s == 9:
                                                o0.configure(image=o9)
                                                o0.update()
                                                time.sleep(0.2)
                                                s += 1
                                                if s == 10:
                                                    o0.configure(image=o10)
                                                    o0.update()
                                                    time.sleep(0.2)
                                                    s += 1
                                                    if s == 11:
                                                        o0.configure(image=o11)
                                                        o0.update()
                                                        time.sleep(0.2)
                                                        s += 1
                                                        if s == 12:
                                                            o0.configure(image=o12)
                                                            o0.update()
                                                            time.sleep(0.2)
                                                            s += 1
                                                            if s == 13:
                                                                o0.configure(image=o13)
                                                                o0.update()
                                                                time.sleep(0.2)
                                                                s += 1
                                                                if s == 14:
                                                                    o0.configure(image=o14)
                                                                    o0.update()
                                                                    time.sleep(0.2)
                                                                    s += 1
                                                                    if s == 15:
                                                                        o0.configure(image=o15)
                                                                        o0.update()
                                                                        time.sleep(0.2)
                                                                        s += 1
                                                                        if s == 16:
                                                                            o0.configure(image=o16)
                                                                            o0.update()
                                                                            time.sleep(0.2)
                                                                            s += 1
                                                                            if s == 17:
                                                                                o0.configure(image=o)
                                                                                o0.update()
                                                                                time.sleep(0.2)
                                                                                s += 1
                                                                                if s == 18:
                                                                                    s = 0
                                                                                    l()

        except Exception:
            pass

l()

root.mainloop()