from moviepy.editor import *
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import sounddevice as sd
from scipy.io.wavfile import write
root = Tk()
root.title('')
root.iconbitmap('movie.ico')
root.resizable(False, False)
root.configure(bg='white')


def k(event):
    try:
        o = filedialog.askopenfilename(title='Open a file', initialdir='/')
        o0 = filedialog.askopenfilename(title='Open a file', initialdir='/')
        clip = VideoFileClip(o)
        clip2 = VideoFileClip(o0)
        final_clip = concatenate_videoclips([clip, clip2])
        final_clip.write_videofile("output.mp4")
        os.startfile("output.mp4")
    except Exception:
        messagebox.showerror('ERROR', 'WRONG FILE CHOICE')
        pass


def k0(event):
    try:
        o = filedialog.askopenfilename(title='Open a sound file', initialdir='/')
        o0 = filedialog.askopenfilename(title='Open a video file', initialdir='/')
        clip2 = VideoFileClip(o0)
        audio_background = AudioFileClip(o)
        s = clip2.set_audio(audio_background)
        s.write_videofile("output1.mp4")
        os.startfile("output1.mp4")
    except Exception:
        messagebox.showerror('ERROR', 'WRONG FILE CHOICE')
        pass


def k1(event):
    try:
        o = filedialog.askopenfilename(title='Open a video file', initialdir='/')
        o0 = filedialog.askopenfilename(title='Open a photo file', initialdir='/')
        video = VideoFileClip(o)
        logo = (ImageClip(o0).set_duration(video.duration).resize(height=50).margin(right=8, top=8, opacity=0).set_pos(("right", "top")))
        final = CompositeVideoClip([video, logo])
        final.write_videofile("output2.mp4")
        os.startfile("output2.mp4")
    except Exception:
        messagebox.showerror('ERROR', 'WRONG FILE CHOICE')
        pass


def k2(event):
    try:
        o = filedialog.askopenfilename(title='select a video file', initialdir='/')
        o0 = messagebox.askyesno('Delete', 'are you sure ?')
        if o0 == 1:
           os.remove(o)
        else:
            pass
    except Exception:
        pass


def k3(event):
    global w
    try:
        o = filedialog.askopenfilename(title='select a video file', initialdir='/')
        w = Tk()
        w.resizable(False, False)
        w.iconbitmap('movie.ico')
        w.title('')
        w.configure(bg='white')
        video = VideoFileClip(o)
        w1 = Label(w, text='Text:', bg='white').grid(row=0, column=0)
        w2 = Label(w, text='FontSize:', bg='white').grid(row=1, column=0)
        w3 = Label(w, text='Color:', bg='white').grid(row=2, column=0)
        w4 = Label(w, text='Font:', bg='white').grid(row=3, column=0)
        w5 = Label(w, text='Position:', bg='white').grid(row=4, column=0)
        w6 = Label(w, text='Duration:', bg='white').grid(row=5, column=0)

        w7 = Entry(w, bg='white')
        w7.grid(row=0, column=1)
        w8 = Entry(w, bg='white')
        w8.grid(row=1, column=1)
        w9 = Entry(w, bg='white')
        w9.grid(row=2, column=1)
        w10 = Entry(w, bg='white')
        w10.grid(row=3, column=1)
        w11 = Entry(w, bg='white')
        w11.grid(row=4, column=1)
        w12 = Entry(w, bg='white')
        w12.grid(row=5, column=1)

        w13 = Label(w, text='ENTER', bg='white')
        w13.grid(row=6, columnspan=2)

        def w0(event):
            try:
                txt_clip = TextClip(str(w7.get()), fontsize=int(w8.get()), color=str(w9.get()), font=str(w10.get())).set_position(str(w11.get())).set_duration(int(w12.get()))

                result = CompositeVideoClip([video, txt_clip])
                result.write_videofile("output3.mp4")
                os.startfile("output3.mp4")
                w.destroy()
            except Exception as plo:
                messagebox.showerror('ERROR', plo)
                pass

        w13.bind('<Button-1>', w0)
        w.mainloop()
    except Exception as plj:
        messagebox.showerror('ERROR', plj)
        w.destroy()
        pass


def k4(event):
    try:
        s = Tk()
        s.title('')
        s.resizable(False, False)
        s.iconbitmap('movie.ico')

        x0 = Label(s, text='Seconds :')
        x0.grid(row=0, column=0)

        x1 = Label(s, text='ENTER')
        x1.grid(row=1, columnspan=2)

        x = Entry(s)
        x.grid(row=0, column=1)

        def x2(event):
            freq = 44100
            duration = int(x.get())
            recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
            sd.wait()
            write("output.wav", freq, recording)
            os.startfile("output.wav")
            s.destroy()

        x1.bind('<Button-1>', x2)
        s.mainloop()
    except Exception:
        messagebox.showerror('ERROR', "COULD'NT RECORD VOICE")
        pass


def r(event):
    p.configure(bg='blue')

    def rk(event):
        p.configure(bg='white')
        p.bind('<Motion>', r)

    p.bind('<Leave>', rk)


def r0(event):
    p0.configure(bg='blue')

    def rk(event):
        p0.configure(bg='white')
        p0.bind('<Motion>', r0)

    p0.bind('<Leave>', rk)


def r1(event):
    p1.configure(bg='blue')

    def rk(event):
        p1.configure(bg='white')
        p1.bind('<Motion>', r1)

    p1.bind('<Leave>', rk)


def r2(event):
    p2.configure(bg='blue')

    def rk(event):
        p2.configure(bg='white')
        p2.bind('<Motion>', r2)

    p2.bind('<Leave>', rk)


def r3(event):
    p3.configure(bg='blue')

    def rk(event):
        p3.configure(bg='white')
        p3.bind('<Motion>', r3)

    p3.bind('<Leave>', rk)


def r4(event):
    p5.configure(bg='blue')

    def rk(event):
        p5.configure(bg='white')
        p5.bind('<Motion>', r4)

    p5.bind('<Leave>', rk)


p4 = Label(root, text='Movie Editor', font=('calibri', 25, 'bold'), fg='red', bg='white')
p4.grid(row=0, column=0)

p = Label(root, text='Stick Videos', font=('calibri', 15, 'bold'), bg='white')
p.grid(row=1, column=0)

p0 = Label(root, text='Put Sound', font=('calibri', 15, 'bold'), bg='white')
p0.grid(row=2, column=0)

p1 = Label(root, text='Put Brand Image', font=('calibri', 15, 'bold'), bg='white')
p1.grid(row=3, column=0)

p3 = Label(root, text='Put text', font=('calibri', 15, 'bold'), bg='white')
p3.grid(row=4, column=0)

p5 = Label(root, text='Record voice', font=('calibri', 15, 'bold'), bg='white')
p5.grid(row=5, column=0)

p2 = Label(root, text='Delete', font=('calibri', 15, 'bold'), bg='white')
p2.grid(row=6, column=0)

p.bind('<Button-1>', k)
p0.bind('<Button-1>', k0)
p1.bind('<Button-1>', k1)
p2.bind('<Button-1>', k2)
p3.bind('<Button-1>', k3)
p5.bind('<Button-1>', k4)
p.bind('<Motion>', r)
p0.bind('<Motion>', r0)
p1.bind('<Motion>', r1)
p2.bind('<Motion>', r2)
p3.bind('<Motion>', r3)
p5.bind('<Motion>', r4)
root.mainloop()