#--------------------------
#遷移ののある場合サンプル
#gui4.py
#--------------------------
import  tkinter as tk

global_var = ""


def wiget_destroy():
    root.destroy()
#-----------------
#認証画面
#-----------------
def first_gui():
    def change_display():
        root.destroy()
        second_gui()
    def btn_click():
		#changeの前に値を入れる
        global_va=txt.get()
        print("uid=",global_va)
        #-------------------------------
        #認証できるかどうか判断する
        #--------------------------------
        
        
        
        
        change_display()
        

    root = tk.Tk()
    root.title("フォーム遷移")
    # 画面サイズ
    root.geometry('300x200')
    # 画面タイトル
    root.title('認証画面')

    # UID
    lbl = tk.Label(text='UID')
    lbl.place(x=30, y=70)

    # UID
    txt = tk.Entry(width=20)
    txt.place(x=90, y=70)

    # PWD
    lbl = tk.Label(text='PWD')
    lbl.place(x=30, y=100)

    # PWD
    txt2 = tk.Entry(width=20)
    txt2.place(x=90, y=100)
    #ボタン
    btn = tk.Button(root, text='実行', command=btn_click)
    btn.place(x=90, y=130) #表示位置

    root.mainloop()
#-------------------
#認証された画面
#--------------------
def second_gui():
    def change_display():
        root.destroy()
        first_gui()

    root = tk.Tk()
    root.title("認証結果")
    # 画面サイズ
    root.geometry('300x200')
    print(global_var)
    # 画面タイトル

    # UID
    lbl = tk.Label(text=global_var+'が認証されました')
    lbl.place(x=30, y=70)
    #ボタン
    btn = tk.Button(root, text='戻る', command=change_display)
    btn.place(x=90, y=130) #表示位置
    root.mainloop()

if __name__ == '__main__':
    first_gui()