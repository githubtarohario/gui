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
#------------
#kensaku
#引数　uid
#---------------    
def kensaku(uid):
    dbname='TestDB.db'
    conn=sqlite3.connect(dbname)
    select_sql = "select uid,pwd from user where uid='"+uid+"'"
    print(select_sql)
    flg=0
    c = conn.cursor()
    for row in c.execute(select_sql):
        print(row[0],"-----",row[1])
        print("OK")
        uid=row[0]
        pwd=row[1]
        txtpwd.insert(tk.END,pwd)
        flg=1
    conn.close()
    if flg==0:
       print("データない")




#-----------------------
# ボタンのイベント
# ------------------------ 
#検索ボタン
def btn_click():
    uid=txtuid.get()
    print(uid)
    kensaku(uid)
#追加ボタン
   
def btn_click2():
    uid=txtuid.get()
    pwd=txtpwd.get()
    print(uid,pwd)
    insertdb(uid,pwd)
#クリアボタン
def btn_click3():
    txtuid.delete(0,tk.END)
    txtpwd.delete(0,tk.END)    
    
    
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
btn1 = tk.Button(root, text='検索', command=btn_click)
btn1.place(x=90, y=160) #表示位置
btn2 = tk.Button(root, text='追加', command=btn_click2)
btn2.place(x=130, y=160) #表示位置

btn3 = tk.Button(root, text='クリア', command=btn_click3)
btn3.place(x=170, y=160) #表示位置




# 表示
root.mainloop()