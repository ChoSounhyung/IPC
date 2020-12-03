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
        self.trv = ttk.Treeview(columns=(1), show="headings", height="10")
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

        home_image = PhotoImage(file='../image/home_btn.png')
        home_click = Button(borderwidth=0, command=self.go_back, bg='#272727', activebackground='#272727')
        home_click.place(x=50, y=600, anchor='nw')
        home_click.config(image=home_image)

        self.window.mainloop()


    def update(self,rows) :
        self.trv.delete(*self.trv.get_children())
        for i in rows:
            self.trv.insert('', 'end', values=i,tag='style')

    #db connect
    def db_connect(self) :
        mydb = pymysql.connect(host="localhost", user="root", password="123456", db="ipc")
        cursor = mydb.cursor()

        query = "SELECT hakbun from student_table where check_mypc = %s"
        cursor.execute(query,("X"))
        rows = cursor.fetchall()
        self.update(rows)

    def go_back(self):
        from gui.teacher_menu import TeacherMenu
        self.window.destroy()
        TeacherMenu()
