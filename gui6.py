#--------------------------
#遷移ののある場合サンプル
#gui4.py
#--------------------------
import  tkinter as tk
import sqlite3

def wiget_destroy():
    root.destroy()
def nisyo(uid,pwd):
    flg=0
    dbname='TestDB.db'
    conn=sqlite3.connect(dbname)
    c = conn.cursor()
    select_sql = "select * from user where uid='"+uid+"' and pwd='"+pwd+"'"
    print(select_sql)
    c.execute(select_sql)
    data=c.fetchall()
    if len(data)==0:
       conn.close()
       return(0)
    conn.close()
    return(1)  


#-----------------
#認証画面
#-----------------
def first_gui():
    def btn_click():
        uid=txt.get()
        pwd=txt2.get()
        print(uid,pwd)
        if(nisyo(uid,pwd)):
            root.destroy()
            second_gui()
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
    # 画面タイトル

    # UID
    lbl = tk.Label(text='遷移しました')
    lbl.place(x=30, y=70)
    #ボタン
    btn = tk.Button(root, text='戻る', command=change_display)
    btn.place(x=90, y=130) #表示位置
    root.mainloop()

if __name__ == '__main__':
    first_gui()