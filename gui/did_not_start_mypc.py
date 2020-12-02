from tkinter import *
from tkinter import ttk
import pymysql

class DidNotStartMyPc :
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#272727')
        self.window.resizable(False, False)
        self.trv = ttk.Treeview(columns=(1, 2, 3, 4), show="headings", height="10")
        self.db_connect()

        did_not_start_mypc = Label(text='내 PC 지키미를 안한 사람', bg='#272727', fg='#51F591',
                                    font=("Arial 15 bold"))
        did_not_start_mypc.place(x=50, y=70)

        self.trv.place(x=50,y=150)

        vsb = ttk.Scrollbar(orient="vertical", command=self.trv.yview)
        self.trv.configure(yscrollcommand=vsb.set)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial 15 bold"))
        style.configure("Treeview", rowheight=40)

        self.trv.tag_configure('style',font=("Arial 15"))

        self.trv.column("#1", width=200, anchor="center")
        self.trv.heading(1, text='학번', anchor="center")

        self.trv.column("#2", width=200, anchor="center")
        self.trv.heading(2, text='이번 달', anchor="center")

        self.trv.column("#3", width=200, anchor="center")
        self.trv.heading(3, text='score', anchor="center")

        self.trv.column("#4", width=300, anchor="center")
        self.trv.heading(4, text='reason', anchor="center")

        self.window.mainloop()


    def update(self,rows) :
        self.trv.delete(*self.trv.get_children())
        for i in rows:
            self.trv.insert('', 'end', values=i,tag='style')


    # 안한 사람 뽑아오기
    # 학번 리스트를 만들어 그 안에 해당하는 학번이 데이터베이스에 존재하지 않으면
    # 학번 가져오기
    #


    #db connect
    def db_connect(self) :
        mydb = pymysql.connect(host="localhost", user="root", password="123456", db="ipc")
        cursor = mydb.cursor()

        query = "SELECT hakbun, this_month, score, reason from mypc_table where score=0"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.update(rows)