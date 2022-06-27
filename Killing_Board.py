from tkinter import *
import time
import random
score = 0
root = Tk()
root.title('score: ' + str(score))
root.resizable(False, False)
gm = Canvas(root, width=400, height=400, bg="grey")
gm.grid()
bouncer = gm.create_rectangle(380, 380, 300, 390, fill="blue")


def balls():
    img0 = PhotoImage(file="block.jpg")
    loc = [0, 50, 100, 150, 200, 250, 300, 350]
    loc0 = random.choice(loc)
    ennemi = gm.create_image(loc0, 0, image=img0)

    while True:
        bouncerc = gm.coords(bouncer)
        if bouncerc[2] == 80:
            gm.move(bouncer, 10, 0)
        if bouncerc[2] == 410:
            gm.move(bouncer, -10, 0)

        def o(event):
            gm.move(bouncer, -10, 0)

        def o0(event):
            gm.move(bouncer, 10, 0)

        def o1(event):
            global score
            root.unbind('<Return>')
            img = PhotoImage(file="rose.jpg")
            k = gm.create_image(bouncerc[2] - 40, bouncerc[1] - 10, image=img)
            p = 10
            gm.move(k, 0, -p)
            gm.update()
            time.sleep(0.1)
            if p == 10:
                p += 10
                gm.move(k, 0, -p)
                gm.update()
                time.sleep(0.1)
                if p == 20:
                    p += 10
                    gm.move(k, 0, -p)
                    gm.update()
                    time.sleep(0.1)
                    if p == 30:
                        p += 10
                        gm.move(k, 0, -p)
                        gm.update()
                        time.sleep(0.1)
                        if p == 40:
                            p += 10
                            gm.move(k, 0, -p)
                            gm.update()
                            time.sleep(0.1)
                            if p == 50:
                                p += 10
                                gm.move(k, 0, -p)
                                gm.update()
                                time.sleep(0.1)
                                if p == 60:
                                    p += 10
                                    gm.move(k, 0, -p)
                                    gm.update()
                                    time.sleep(0.1)
                                    if p == 70:
                                        p += 10
                                        gm.move(k, 0, -p)
                                        gm.update()
                                        time.sleep(0.1)
                                        k0 = gm.coords(k)
                                        if k0[0] <= loc0 + 70 and k0[0] >= loc0 - 70:
                                            gm.delete(ennemi)
                                            gm.delete(k)
                                            score += 1
                                            root.title('score: ' + str(score))
                                            balls()
                                        elif k0[0] != loc0 + 70 and k0[0] != loc0 - 70:
                                            gm.delete(k)
                                            score -= 1
                                            root.title('score: ' + str(score))

        root.bind('<Left>', o)
        root.bind('<Right>', o0)
        root.bind('<Return>', o1)
        time.sleep(0.01)
        root.update()


balls()
root.mainloop()
