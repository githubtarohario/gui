#---------------------------
#課題１の回答
#---------------------------

from tkinter import ttk #combox
import tkinter as tk

#-----------------------
# ボタンのイベント
# ------------------------ 
def btn_click():
    print("認証")

# Tkクラス生成
root = tk.Tk()
# 画面サイズ
root.geometry('300x200')
# 画面タイトル
root.title('認証画面')

# UID ラベル
lbl = tk.Label(text='UID')
lbl.place(x=30, y=70)

# UIDテキストボックス
txt = tk.Entry(width=20)
txt.place(x=90, y=70)

# PWDラベル
lbl = tk.Label(text='PWD')
lbl.place(x=30, y=100)

# PWDテキストボックス
txt = tk.Entry(width=20)
txt.place(x=90, y=100)
#ボタン
btn = tk.Button(root, text='実行', command=btn_click)
btn.place(x=90, y=130) #表示位置

root.mainloop()