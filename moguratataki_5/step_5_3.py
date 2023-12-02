import tkinter
import random

FNT = ("System", 40)
holes = [0, 0, 0, 0, 0]

def main(): # メイン処理を行う関数
    cvs.delete("all")
    for i in range(5):
        x = 200*i+100
        cvs.create_image(x, 160, image=img[holes[i]])
        cvs.create_text(x, 280, text=i+1, font=FNT, fill="yellow")

    r = random.randint(0,4)
    if holes[r]==0:
        holes[r] = 1
    else:
        holes[r] = 0

    root.after(330, main)

root = tkinter.Tk()
cvs = tkinter.Canvas(width=1000, height=320)
cvs.pack()
img = [
    tkinter.PhotoImage(file="image/hole.png"),
    tkinter.PhotoImage(file="image/mole.png"),
    tkinter.PhotoImage(file="image/hit.png")
]
ham = tkinter.PhotoImage(file="image/hammer.png")
main()
root.mainloop()
