import time
from tkinter import *
from datetime import datetime
root = Tk()
root.geometry('280x70')
root.title('')
root.resizable(False, False)
root.iconbitmap('o.ico')
s = 0
o0 = Label(root, text='C', font=('calibri', 40, 'bold'))
o0.place(x=0, y=0)
o1 = Label(root, text='O', font=('calibri', 40, 'bold'))
o1.place(x=80, y=0)
o2 = Label(root, text='O', font=('calibri', 40, 'bold'))
o2.place(x=160, y=0)
o3 = Label(root, text='L', font=('calibri', 40, 'bold'))
o3.place(x=240, y=0)

if str(datetime.today().strftime("%p")) == 'AM':
  root.configure(bg='cyan')
  o0.configure(bg='cyan')
  o1.configure(bg='cyan')
  o2.configure(bg='cyan')
  o3.configure(bg='cyan')
elif str(datetime.today().strftime("%p")) == 'PM':
  root.configure(bg='blue')
  o0.configure(bg='blue')
  o1.configure(bg='blue')
  o2.configure(bg='blue')
  o3.configure(bg='blue')



while True:

    def l():
      try:
        global s, o0, o1, o2, o3
        s += 1

        if s == 1:
          o0.configure(fg='red')
          o0.update()
          time.sleep(0.1)
          s += 1
          if s == 2:
            o1.configure(fg='red')
            o0.configure(fg='black')
            o1.update()
            time.sleep(0.1)
            s += 1
            if s == 3:
              o1.configure(fg='black')
              o2.configure(fg='red')
              o2.update()
              time.sleep(0.1)
              s += 1
              if s == 4:
                o2.configure(fg='black')
                o3.configure(fg='red')
                o3.update()
                time.sleep(0.1)
                s += 1
                if s == 5:
                  o3.configure(fg='black')
                  s = 0
                  l()
      except Exception:
        quit()
    l()
    root.mainloop()