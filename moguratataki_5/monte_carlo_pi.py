import tkinter
import random

root = tkinter.Tk()
cvs = tkinter.Canvas(width=600, height=600, bg="black")
cvs.pack()

pi = 0
c = 0
for i in range(1, 5001):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    col = "red"
    if x*x+y*y<=300*300:
        c = c + 1
        col = "cyan"
    cvs.create_rectangle(x+300, y+300, x+302, y+302, fill=col, width=0)
    cvs.update()
    pi = 4*c/i
    root.title("円周率 "+str(pi))

root.mainloop()
