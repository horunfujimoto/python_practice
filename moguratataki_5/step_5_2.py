import tkinter

FNT = ("System", 40)
holes = [1, 0, 2, 0, 1]

def main(): # メイン処理を行う関数
    for i in range(5):
        x = 200*i+100
        cvs.create_image(x, 160, image=img[holes[i]])
        cvs.create_text(x, 280, text=i+1, font=FNT, fill="yellow")

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
