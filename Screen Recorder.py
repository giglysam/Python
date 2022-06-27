import os
import pyautogui
import cv2
import numpy as np
import keyboard
from tkinter import *
from tkinter import messagebox


def screen():
    root = Tk()
    root.resizable(False, False)
    root.title('')
    a = Label(root, text='Screen Recording', font=('calibri', 15, 'bold'))
    a.grid(row=0, column=0)

    a0 = Label(root, text='⚫', fg='red', font=('calibri', 10, 'bold'))
    a0.grid(row=0, column=1)

    a1 = Label(root, text='Recording.avi', font=('calibri', 10, 'bold'))
    a1.grid(row=1, column=0)

    a2 = Label(root, text='🗑️', font=('calibri', 10, 'bold'))
    a2.grid(row=1, column=1)

    def a3(event):
        try:
            root.destroy()

            resolution = (1920, 1080)

            codec = cv2.VideoWriter_fourcc(*"XVID")

            filename = "Recording.avi"

            fps = 10

            out = cv2.VideoWriter(filename, codec, fps, resolution)

            while True:
                img = pyautogui.screenshot()

                frame = np.array(img)

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                out.write(frame)

                if keyboard.is_pressed('x'):
                    screen()
                    break

            out.release()
            cv2.destroyAllWindows()
        except Exception:
            messagebox.showerror('ERROR', "Can't Start Recording")

    def a4(event):
        try:
            os.startfile('Recording.avi')
        except Exception:
            messagebox.showerror('ERROR', 'No Such File')

    def a5(event):
        try:
            o = messagebox.askyesno('Delete', 'Do You Want To Delete This File ?')
            if o == 1:
                os.remove('Recording.avi')
            else:
                pass
        except Exception:
            messagebox.showerror('ERROR', 'No Such File')

    a0.bind('<Button-1>', a3)
    a1.bind('<Double-Button-1>', a4)
    a2.bind('<Button-1>', a5)
    root.mainloop()


screen()