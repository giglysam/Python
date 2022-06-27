from tkinter import *
x = 110
y = 110
w = input('> ')
root = Tk()
root.resizable(False, False)
root.geometry('250x250')


def game():
    global x, y
    snake = Label(root, bg=w)
    snake.place(x=x, y=y)

    def up(event):
        try:
            global y, x
            y -= 2
            snake.place(x=x, y=y)
            snake.update()
            Label(root, bg=w).place(x=x, y=y)
            if y == 0:
                snake.destroy()
                x = 110
                y = 110
                game()
            if y == y:
                up(event)
        except Exception:
            pass

    def down(event):
        try:
            global y, x
            y += 2
            snake.place(x=x, y=y)
            snake.update()
            Label(root, bg=w).place(x=x, y=y)
            if y == 230:
                snake.destroy()
                x = 110
                y = 110
                game()
            if y == y:
                down(event)
        except Exception:
            pass

    def left(event):
        try:
            global x, y
            x -= 2
            snake.place(x=x, y=y)
            snake.update()
            Label(root, bg=w).place(x=x, y=y)
            if x == 0:
                snake.destroy()
                x = 110
                y = 110
                game()
            if x == x:
                left(event)
        except Exception:
            pass

    def right(event):
        try:
            global x, y
            x += 2
            snake.place(x=x, y=y)
            snake.update()
            Label(root, bg=w).place(x=x, y=y)
            if x == 230:
                snake.destroy()
                x = 110
                y = 110
                game()
            if x == x:
                right(event)
        except Exception:
            pass

    root.bind('<Up>', up)
    root.bind('<Down>', down)
    root.bind('<Left>', left)
    root.bind('<Right>', right)
    root.mainloop()


game()