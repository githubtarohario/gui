#---------------------------
#combox付け加える
#---------------------------



from tkinter impor tk
from tkinter import ttk

def cb_selected(event):
    print(v1.get())



# Tkクラス生成
root = tk.Tk()
# 画面サイズ
root.geometry('300x200')
# 画面タイトル
root.title('認証画面')

# Combobox
v1 = StringVar()
txt = StringVar()

cb = ttk.Combobox(root, textvariable=v1)
cb.place(x=90,y=10)
cb.bind('<<ComboboxSelected>>', cb_selected)
cb['values']=('管理者', '総務', '一般')
cb.set("管理者")


#cb.grid(row=0, column=0)
# 表示
root.mainloop()