import tkinter
import random

FNT = ("System", 40)
holes = [0, 0, 0, 0, 0]
key = ""

def pkey(e): # キーを押した時に呼ぶ関数
    global key
    key = e.keysym

def main(): # メイン処理を行う関数
    global key

    cvs.delete("all")
    for i in range(5):
        x = 200*i+100
        cvs.create_image(x, 160, image=img[holes[i]])
        cvs.create_text(x, 280, text=i+1, font=FNT, fill="yellow")
        if holes[i]==2: holes[i] = 0

    r = random.randint(0,4)
    holes[r] = 1

    if "1"<=key and key<="5":
        m = int(key)-1
        x = m*200+100
        cvs.create_image(x, 60, image=ham)
        if holes[m]==1: holes[m] = 2

    key = ""
    root.after(330, main)

root = tkinter.Tk()
root.bind("<Key>", pkey)
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
