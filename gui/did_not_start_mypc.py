from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

class DidNotStartMyPc :
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#272727')
        self.window.resizable(False, False)

#db connect
mydb = pymysql.connect(host="localhost", user="root", password="123456", db="ipc")
cursor = mydb.cursor()

root = Tk()
q = StringVar()
wrapper = LabelFrame(root,text="내 PC 지키미")
wrapper2 = LabelFrame(root,text="버튼 메뉴")
wrapper3 = LabelFrame(root,text="Search")

wrapper.pack(fill="both",expand="yes",padx=20,pady=10)
wrapper2.pack(fill="both",expand="yes",padx=20,pady=10)
wrapper3.pack(fill="both",expand="yes",padx=20,pady=10)

trv = ttk.Treeview(wrapper, columns=(1,2,3,4), show="headings", height="10")
trv.pack()

trv.column("#1",width=100,anchor="center")
trv.heading(1, text='학번',anchor="center")

trv.column("#2",width=100,anchor="center")
trv.heading(2, text='이번 달',anchor="center")

trv.column("#3",width=100,anchor="center")
trv.heading(3, text='score',anchor="center")

trv.column("#4",width=200,anchor="center")
trv.heading(4, text='reason',anchor="center")

query = "SELECT hakbun, this_month, score, reason from mypc_table where score=0"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)

#버튼 메뉴 부분 속성들
lbl = Label(wrapper2, text="버튼 메뉴")
lbl.place(x=10,y=10,anchor='nw')
btn1 = Button(wrapper2, text="내 PC지키미 안한 사람 보기", command=search)
btn1.place(x=80,y=10,anchor='nw')
clear_btn = Button(wrapper2, text="전체 데이터 보기", command=clear)
clear_btn.place(x=250,y=10,anchor='nw')

root.title("MY PC")
root.geometry("600x700")
root.mainloop()