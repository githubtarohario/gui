#---------------------------
#combox付け加える
#---------------------------
from tkinter import ttk #combox
import tkinter as tk
from tkinter import *   #必要
import sqlite3 

#------------------
#insertdb
#-------------------
def insertdb(uid,pwd):
    dbname='TestDB.db'
    conn=sqlite3.connect(dbname)
    c = conn.cursor()
    sql = 'INSERT INTO user(uid,pwd) VALUES(?,?)'
    data = (uid,pwd)
    c.execute(sql, data)
    conn.commit()
    conn.close()
    print("追加しました。")
    #テキストボックスクリア
    txtuid.delete(0,tk.END)
    txtpwd.delete(0,tk.END)
def kensaku(uid):
    dbname='TestDB.db'
    conn=sqlite3.connect(dbname)
    select_sql = "select uid,pwd from user where uid='"+uid+"'"
    print(select_sql)
    c = conn.cursor()
    for row in c.execute(select_sql):
        print(row[0],row[1])
        print("OK")
        uid=row[0]
        pwd=row[1]
        #txtuid.insert(tk.END,uid)
        txtpwd.insert(tk.END,pwd)
    conn.close()




def cb_selected(event):
    print('v1 = %s' % v1.get())
#-----------------------
# ボタンのイベント
# ------------------------ 
def btn_click():
    #テキストボックスに文字列abcを挿入
    #messagebox.showinfo("メッセージ", "ボタンがクリックされました")
    #txt.insert(tk.END,"認証")
    uid=txtuid.get()
    pwd=txtpwd.get()
    print(uid,pwd)
    #insertdb(uid,pwd)
    kensaku(uid)
    
def btn_click2():
    uid=txtuid.get()
    pwd=txtpwd.get()
    print(uid,pwd)
    insertdb(uid,pwd)
    
    
    
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
txtuid = tk.Entry(width=20)
txtuid.place(x=90, y=70)
# PWD(label)
lbl = tk.Label(text='PWD')
lbl.place(x=30, y=100)
# PWD(textbix)
txtpwd = tk.Entry(width=20)
txtpwd.place(x=90, y=100)
#ボタン
btn = tk.Button(root, text='検索', command=btn_click)
btn.place(x=90, y=160) #表示位置
btn = tk.Button(root, text='追加', command=btn_click2)
btn.place(x=130, y=160) #表示位置





# 表示
root.mainloop()