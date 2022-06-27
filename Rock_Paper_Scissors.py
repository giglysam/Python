from tkinter import *
import time
import random
time0 = 0
root = Tk()
root.resizable(False, False)
root.iconbitmap('o.ico')
root.title('Score: ')
HOME = LabelFrame(root)
HOME.grid(row=0, column=0)
TITLE = Label(HOME, text='Rock, Paper, Scissors', font=("algerian", 20, 'bold')).grid(row=0, column=0)
GO = Label(HOME, text='Start', font=("calibri", 15, 'bold'), fg='red')
GO.grid(row=1, column=0)
INPUT = LabelFrame(root)
R1 = Label(INPUT, font=("algerian", 50, 'bold'))
R1.grid(row=0, column=0, columnspan=3)
R2 = Label(INPUT, font=("algerian", 30, 'bold'))
R3 = Label(INPUT, font=("algerian", 30, 'bold'))
R4 = Label(INPUT, font=("algerian", 30, 'bold'))
R5 = Label(root, font=("algerian", 30, 'bold'))
R = '🗿'
P = '🧻'
C = '✂'
RD = [R, P, C]


def Game(event):
    global time0
    HOME.grid_forget()
    INPUT.grid(row=0, column=0)
    R1.configure(text='🗿', fg='blue')
    R1.update()
    time.sleep(1)
    time0 += 1
    if time0 == 1:
        R1.configure(text='🧻', fg='black')
        R1.update()
        time.sleep(1)
        time0 += 1
        if time0 == 2:
            R1.configure(text='✂', fg='red')
            R1.update()
            time.sleep(1)
            time0 += 1
            if time0 == 3:
                R1.configure(text='SHOOT', fg='violet')
                R1.update()
                R2.grid(row=1, column=0)
                R3.grid(row=1, column=1)
                R4.grid(row=1, column=2)
                R2.configure(text='🗿', fg='blue')
                R3.configure(text='🧻', fg='black')
                R4.configure(text='✂', fg='red')

                def P2(event):
                    if random.choice(RD) == R2.cget('text'):
                        INPUT.grid_forget()
                        R5.configure(text='🗿 <<Draw>> 🗿', fg='gray')
                        R5.grid(row=1, column=2)
                        root.title('Score: Draw')

                        def H(event):
                            R5.grid_forget()
                            HOME.grid(row=0, column=0)
                            R2.grid_forget()
                            R3.grid_forget()
                            R4.grid_forget()

                        root.bind('<Return>', H)
                    elif random.choice(RD) != R2.cget('text'):
                        if random.choice(RD) == '🧻':
                            INPUT.grid_forget()
                            R5.configure(text='🧻 <<Lost>> 🧻', fg='red')
                            R5.grid(row=1, column=2)
                            root.title('Score: Lost')

                            def H(event):
                                R5.grid_forget()
                                HOME.grid(row=0, column=0)
                                R2.grid_forget()
                                R3.grid_forget()
                                R4.grid_forget()

                            root.bind('<Return>', H)
                        elif random.choice(RD) == '✂':
                            INPUT.grid_forget()
                            R5.configure(text='✂ <<Won>> ✂', fg='lime')
                            R5.grid(row=1, column=2)
                            root.title('Score: Win')

                            def H(event):
                                R5.grid_forget()
                                HOME.grid(row=0, column=0)
                                R2.grid_forget()
                                R3.grid_forget()
                                R4.grid_forget()

                            root.bind('<Return>', H)

                def P3(event):
                    if random.choice(RD) == R3.cget('text'):
                        INPUT.grid_forget()
                        R5.configure(text='🧻 <<Draw>> 🧻', fg='gray')
                        R5.grid(row=1, column=2)
                        root.title('Score: Draw')

                        def H(event):
                            R5.grid_forget()
                            HOME.grid(row=0, column=0)
                            R2.grid_forget()
                            R3.grid_forget()
                            R4.grid_forget()

                        root.bind('<Return>', H)
                    elif random.choice(RD) != R3.cget('text'):
                        if random.choice(RD) == '✂':
                            INPUT.grid_forget()
                            R5.configure(text='✂ <<Lost>> ✂', fg='red')
                            R5.grid(row=1, column=2)
                            root.title('Score: Lost')

                            def H(event):
                                R5.grid_forget()
                                HOME.grid(row=0, column=0)
                                R2.grid_forget()
                                R3.grid_forget()
                                R4.grid_forget()

                            root.bind('<Return>', H)
                        elif random.choice(RD) == '🗿':
                            INPUT.grid_forget()
                            R5.configure(text='🗿 <<Won>> 🗿', fg='lime')
                            R5.grid(row=1, column=2)
                            root.title('Score: Win')

                            def H(event):
                                R5.grid_forget()
                                HOME.grid(row=0, column=0)
                                R2.grid_forget()
                                R3.grid_forget()
                                R4.grid_forget()

                            root.bind('<Return>', H)

                def P4(event):
                    if random.choice(RD) == R4.cget('text'):
                        INPUT.grid_forget()
                        R5.configure(text='✂ <<Draw>> ✂', fg='gray')
                        R5.grid(row=1, column=2)
                        root.title('Score: Draw')

                        def H(event):
                            R5.grid_forget()
                            HOME.grid(row=0, column=0)
                            R2.grid_forget()
                            R3.grid_forget()
                            R4.grid_forget()

                        root.bind('<Return>', H)
                    elif random.choice(RD) != R4.cget('text'):
                        if random.choice(RD) == '🗿':
                            INPUT.grid_forget()
                            R5.configure(text='🗿 <<Lost>> 🗿', fg='red')
                            R5.grid(row=1, column=2)
                            root.title('Score: Lost')

                            def H(event):
                                R5.grid_forget()
                                HOME.grid(row=0, column=0)
                                R2.grid_forget()
                                R3.grid_forget()
                                R4.grid_forget()

                            root.bind('<Return>', H)
                        elif random.choice(RD) == '🧻':
                            INPUT.grid_forget()
                            R5.configure(text='🧻 <<Won>> 🧻', fg='lime')
                            R5.grid(row=1, column=2)
                            root.title('Score: Win')

                            def H(event):
                                R5.grid_forget()
                                HOME.grid(row=0, column=0)
                                R2.grid_forget()
                                R3.grid_forget()
                                R4.grid_forget()

                            root.bind('<Return>', H)

                R2.bind('<Button-1>', P2)
                R3.bind('<Button-1>', P3)
                R4.bind('<Button-1>', P4)
                time0 = 0


GO.bind('<Button-1>', Game)
root.mainloop()