from tkinter import *
from tkinter import ttk
 
#-------------------------------------
#コンボボックスを押したときのイベント
#-----------------------------------------
def select_cb(event):
    print(txt.get())

root = Tk()
root.title('test')
root.geometry('300x200')

#--------------------------------
#コンボボックス
#--------------------------------------
txt = StringVar()
cb = ttk.Combobox(root, textvariable=txt)
cb.place(x=90,y=10)
cb.bind('<<ComboboxSelected>>' , select_cb)
cb['values']=('管理者', '総務', '一般')
cb.set("管理者")
 
root.mainloop()
 
print(txt.get())