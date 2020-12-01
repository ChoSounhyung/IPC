from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import pymysql

def latest_search():
    q2 = q.get()
    query = "SELECT * from mypc_table where hakbun = %s"
    cursor.execute(query,(q2))
    rows = cursor.fetchall()

    data_list = list(rows[0])
    hakbun = data_list[0]
    this_month = str(datetime.datetime.today().year) +'.'+ data_list[1]
    score = data_list[2]
    reason = data_list[3]

    this_month_lbl = Label(wrapper, text=this_month)
    this_month_lbl.place(x=10, y=60, anchor='nw')
    hakbun_lbl = Label(wrapper, text=hakbun)
    hakbun_lbl.place(x=80, y=60, anchor='nw')
    score_lbl = Label(wrapper, text=score)
    score_lbl.place(x=140, y=60, anchor='nw')
    reason_lbl = Label(wrapper, text=reason)
    reason_lbl.place(x=180, y=60, anchor='nw')







def clear():
    query = "SELECT hakbun, this_month, score, reason from mypc_table"
    cursor.execute(query)
    rows = cursor.fetchall()

#db connect
mydb = pymysql.connect(host="localhost", user="root", password="123456", db="ipc")
cursor = mydb.cursor()

root = Tk()
q = StringVar()
wrapper = LabelFrame(root,text="이번 달 결과 보기")
wrapper2 = LabelFrame(root,text="점수 입력하기")

wrapper.pack(fill="both",expand="yes",padx=20,pady=10)
wrapper2.pack(fill="both",expand="yes",padx=20,pady=10)

#이번 달 결과 보기
lbl = Label(wrapper, text="이번 달 결과 보기")
lbl.place(x=10,y=10,anchor='nw')
hakbun_lbl = Label(wrapper, text='학번 입력')
hakbun_lbl.place(x=10,y=40,anchor='nw')
ent = Entry(wrapper, textvariable = q)
ent.place(x=80,y=40,anchor='nw')
search_btn = Button(wrapper, text="검색", command=latest_search)
search_btn.place(x=240,y=35,anchor='nw')

root.title("MY PC")
root.geometry("600x400")
root.mainloop()