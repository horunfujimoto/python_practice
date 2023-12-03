import tkinter
import random

# フォントの設定
FNT = ("System", 40)

# モグラの穴の状態を管理するリスト
holes = [0, 0, 0, 0, 0]

# ゲームの状態を表す変数
scene = "タイトル"

# スコアと時間
score = 0
time = 0

# キー入力を受け取る変数
key = ""

# キー入力イベントハンドラ
def pkey(e):
    global key
    key = e.keysym

# メイン処理を行う関数
def main():
    global scene, score, time, key

    # Canvasをクリア
    cvs.delete("all")

    # モグラの穴を描画
    for i in range(5):
        x = 200*i + 100
        cvs.create_image(x, 160, image=img[holes[i]])
        cvs.create_text(x, 280, text=i+1, font=FNT, fill="yellow")

        # モグラが叩かれた状態の場合、穴を空ける
        if holes[i] == 2:
            holes[i] = 0

    # スコアと時間の表示
    cvs.create_text(200, 30, text="SCORE "+str(score), font=FNT, fill="white")
    cvs.create_text(800, 30, text="TIME "+str(time), font=FNT, fill="yellow")

    # タイトル画面の場合
    if scene == "タイトル":
        cvs.create_text(500, 100, text="Mogura Tataki Game", font=FNT, fill="pink")
        cvs.create_text(500, 200, text="[S]tart", font=FNT, fill="cyan")

        # スタートキーが押された場合、ゲームスタート
        if key == "s":
            scene = "ゲーム"
            score = 0
            time = 100

    # ゲーム中の場合
    if scene == "ゲーム":
        # ランダムにモグラが出現する穴を選択
        r = random.randint(0, 4)
        holes[r] = 1

        # キーが1から5の範囲内で、モグラが出現している穴が叩かれた場合
        if "1" <= key and key <= "5":
            m = int(key) - 1
            x = m * 200 + 100
            cvs.create_image(x, 60, image=ham)

            if holes[m] == 1:
                # モグラがいた場合、スコアを加算
                holes[m] = 2
                score = score + 100
            elif holes[m] == 0:
                # モグラがいなかった場合、時間を減少
                time = time - 9
                if time < 1:
                    time = 1
                cvs.create_text(x, 50, text="Miss!", font=FNT, fill="cyan")

        # 残り時間を減少
        time = time - 1

        # 時間が0になった場合、ゲームオーバー
        if time == 0:
            scene = "ゲームオーバー"

    # ゲームオーバー画面の場合
    if scene == "ゲームオーバー":
        cvs.create_text(500, 100, text="GAME END", font=FNT, fill="red")
        cvs.create_text(500, 200, text="[R]eplay", font=FNT, fill="lime")

        # リプレイキーが押された場合、ゲーム再スタート
        if key == "r":
            scene = "ゲーム"
            score = 0
            time = 100

    # キーをリセット
    key = ""

    # 次のフレームを約1/3秒後に実行
    root.after(330, main)

# ウィンドウの作成
root = tkinter.Tk()
root.title("モグラ叩きゲーム 改良版")
root.resizable(False, False)

# キーイベントのバインディング
root.bind("<Key>", pkey)

# Canvasの作成
cvs = tkinter.Canvas(width=1000, height=320)
cvs.pack()

# 画像のロード
img = [
    tkinter.PhotoImage(file="image/hole.png"),
    tkinter.PhotoImage(file="image/mole.png"),
    tkinter.PhotoImage(file="image/hit.png")
]
ham = tkinter.PhotoImage(file="image/hammer.png")

# メインループの開始
main()
root.mainloop()
