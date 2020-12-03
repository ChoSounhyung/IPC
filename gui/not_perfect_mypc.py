import datetime
from tkinter import *
from tkinter import ttk
import pymysql

class NotPerfectMypc :
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#272727')
        self.window.resizable(False, False)
        self.trv = ttk.Treeview(columns=(1, 2, 3, 4), show="headings", height="10")
        self.db_connect()

        did_not_start_mypc = Label(text='100점이 아닌사람', bg='#272727', fg='#51F591',
                                   font=("Arial 15 bold"))
        did_not_start_mypc.place(x=50, y=70)

        self.trv.place(x=50, y=150)

        vsb = ttk.Scrollbar(self.window, orient="vertical", command=self.trv.yview)
        vsb.place(x=730 + 200 + 2, y=150, height=200 + 20)

        self.trv.configure(yscrollcommand=vsb.set)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial 15 bold"))
        style.configure("Treeview", rowheight=40)

        self.trv.tag_configure('style', font=("Arial 15"))

        self.trv.column("#1", width=200, anchor="center")
        self.trv.heading(1, text='학번', anchor="center")

        self.trv.column("#2", width=200, anchor="center")
        self.trv.heading(2, text='제출 시간', anchor="center")

        self.trv.column("#3", width=200, anchor="center")
        self.trv.heading(3, text='score', anchor="center")

        self.trv.column("#4", width=300, anchor="center")
        self.trv.heading(4, text='reason', anchor="center")

        home_image = PhotoImage(file='../image/home_btn.png')
        home_click = Button(borderwidth=0, command=self.go_back, bg='#272727', activebackground='#272727')
        home_click.place(x=50, y=600, anchor='nw')
        home_click.config(image=home_image)

        self.window.mainloop()

    def update(self, rows):
        self.trv.delete(*self.trv.get_children())
        for i in rows:
            self.trv.insert('', 'end', values=i, tag='style')

        # db connect

    def db_connect(self):
        mydb = pymysql.connect(host="localhost", user="root", password="123456", db="ipc")
        cursor = mydb.cursor()

        query = "SELECT hakbun, this_month, score, reason from mypc_table where 0<score and score<100 and this_month like %s"

        now = datetime.datetime.now()
        this_month = str(now.strftime('%Y-%m'))+"%"
        cursor.execute(query,(this_month))
        rows = cursor.fetchall()
        self.update(rows)

    def go_back(self):
        from gui.teacher_menu import TeacherMenu
        self.window.destroy()
        TeacherMenu()