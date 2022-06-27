from tkinter import *
root = Tk()
root.title('')
root.resizable(False, False)
c1 = PhotoImage(file='labir.png')


def game():
    global gx, gy, c1
    gx = 160
    gy = 380
    pg = LabelFrame(root)
    pg.grid(row=0, column=0)
    bg = Label(pg, image=c1)
    bg.grid(row=0, column=0)
    gun = Label(root, bg='black', width=3, height=1)
    gun.place(x=gx, y=gy)

    def leftgun(event):
        global gx, gy
        gx -= 20
        gun.place(x=gx, y=gy)
        if gy == 280 and gx >= 40 and gx <= 320 or gy == 300 and gx >= 40 and gx <= 320:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gx >= 320 and gx <= 380 and gy == 180 or gx >= 320 and gx <= 380 and gy == 200:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gx >= 0 and gx <= 60 and gy == 180 or gx >= 0 and gx <= 60 and gy == 200:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gy == 380 and gx <= 80 and gx >= 0 or gy == 380 and gx <= 380 and gx >= 180:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gy == 300 and gx <= 320 and gx >= 40 or gy == 280 and gx <= 320 and gx >= 40:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gy == 80 and gx <= 320 and gx >= 40 or gy == 100 and gx <= 320 and gx >= 40:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gy == 0 and gx <= 200 and gx >= 0 or gy == 0 and gx <= 380 and gx >= 280:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gx == 200 and gy <= 280 and gy >= 120 or gx == 180 and gy <= 280 and gy >= 120:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gx == 360 or gx == 0:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gy == 0 and gx < 280 and gx > 200:
            gun.place(x=160, y=380)
            root.title('WIN')
            game()

    def rightgun(event):
        global gx, gy
        gx += 20
        gun.place(x=gx, y=gy)
        if gy == 280 and gx >= 40 and gx <= 320 or gy == 300 and gx >= 40 and gx <= 320:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gx >= 320 and gx <= 380 and gy == 180 or gx >= 320 and gx <= 380 and gy == 200:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gx >= 0 and gx <= 60 and gy == 180 or gx >= 0 and gx <= 60 and gy == 200:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gy == 380 and gx <= 80 and gx >= 0 or gy == 380 and gx <= 380 and gx >= 180:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gy == 300 and gx <= 320 and gx >= 40 or gy == 280 and gx <= 320 and gx >= 40:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gy == 80 and gx <= 320 and gx >= 40 or gy == 100 and gx <= 320 and gx >= 40:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gy == 0 and gx <= 200 and gx >= 0 or gy == 0 and gx <= 380 and gx >= 280:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gx == 200 and gy <= 280 and gy >= 120 or gx == 180 and gy <= 280 and gy >= 120:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gx == 360 or gx == 0:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gy == 0 and gx < 280 and gx > 200:
            gun.place(x=160, y=380)
            root.title('WIN')
            game()

    def upgun(event):
        global gx, gy
        gy -= 20
        gun.place(x=gx, y=gy)
        if gy == 280 and gx >= 40 and gx <= 320 or gy == 300 and gx >= 40 and gx <= 320:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gx >= 320 and gx <= 380 and gy == 180 or gx >= 320 and gx <= 380 and gy == 200:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gx >= 0 and gx <= 60 and gy == 180 or gx >= 0 and gx <= 60 and gy == 200:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gy == 380 and gx <= 80 and gx >= 0 or gy == 380 and gx <= 380 and gx >= 180:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gy == 300 and gx <= 320 and gx >= 40 or gy == 280 and gx <= 320 and gx >= 40:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gy == 80 and gx <= 320 and gx >= 40 or gy == 100 and gx <= 320 and gx >= 40:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gy == 0 and gx <= 200 and gx >= 0 or gy == 0 and gx <= 380 and gx >= 280:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gx == 200 and gy <= 280 and gy >= 120 or gx == 180 and gy <= 280 and gy >= 120:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gx == 360 or gx == 0:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gy == 0 and gx < 280 and gx > 200:
            gun.place(x=160, y=380)
            root.title('WIN')
            game()

    def downgun(event):
        global gy, gx
        gy += 20
        gun.place(x=gx, y=gy)
        if gy == 280 and gx >= 40 and gx <= 320 or gy == 300 and gx >= 40 and gx <= 320:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gx >= 320 and gx <= 380 and gy == 180 or gx >= 320 and gx <= 380 and gy == 200:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gx >= 0 and gx <= 60 and gy == 180 or gx >= 0 and gx <= 60 and gy == 200:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gy == 380 and gx <= 80 and gx >= 0 or gy == 380 and gx <= 380 and gx >= 180:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gy == 300 and gx <= 320 and gx >= 40 or gy == 280 and gx <= 320 and gx >= 40:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gy == 80 and gx <= 320 and gx >= 40 or gy == 100 and gx <= 320 and gx >= 40:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gy == 0 and gx <= 200 and gx >= 0 or gy == 0 and gx <= 380 and gx >= 280:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gx == 200 and gy <= 280 and gy >= 120 or gx == 180 and gy <= 280 and gy >= 120:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gx == 360 or gx == 0:
            gun.place(x=160, y=380)
            root.title('LOST')
            game()
        elif gy == 0 and gx < 280 and gx > 200:
            gun.place(x=160, y=380)
            root.title('WIN')
            game()

    root.bind('<Left>', leftgun)
    root.bind('<Right>', rightgun)
    root.bind('<Up>', upgun)
    root.bind('<Down>', downgun)
    root.mainloop()


game()