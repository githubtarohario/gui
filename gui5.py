#---------------------------
#combox付け加える
#---------------------------
from tkinter import ttk #combox
import tkinter as tk
from tkinter import *#必要

def cb_selected(event):
    print('v1 = %s' % v1.get())
#-----------------------
# ボタンのイベント
# ------------------------ 
def btn_click():
    #テキストボックスに文字列abcを挿入
    #messagebox.showinfo("メッセージ", "ボタンがクリックされました")
    txt.insert(tk.END,"認証")
# Tkクラス生成
root = tk.Tk()
# 画面サイズ
root.geometry('300x200')
# 画面タイトル
root.title('認証画面')
# UID(label)
lbl = tk.Label(text='UID')
lbl.place(x=30, y=70)
# UID(textbix)
txt = tk.Entry(width=20)
txt.place(x=90, y=70)
# PWD(label)
lbl = tk.Label(text='PWD')
lbl.place(x=30, y=100)
# PWD(textbix)
txt = tk.Entry(width=20)
txt.place(x=90, y=100)
#ボタン
btn = tk.Button(root, text='実行', command=btn_click)
btn.place(x=90, y=160) #表示位置
# Combobox
v1 = StringVar()
cb = ttk.Combobox(root, textvariable=v1)
cb.place(x=90,y=130)
cb.bind('<<ComboboxSelected>>', cb_selected)
cb['values']=('管理者', '総務', '一般')
cb.set("管理者")
# 表示
root.mainloop()