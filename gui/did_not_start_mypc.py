import datetime
from tkinter import *
from tkinter import ttk

from DB.db_connect import DbConnect
from model.cal_time import CalTime

db_connect = DbConnect()

class DidNotStartMyPc :
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#ffffff')
        self.window.resizable(False, False)
        self.trv = ttk.Treeview(columns=(1), show="headings", height="10")
        self.db_connect()

        did_not_start_mypc = Label(text='내 PC 지키미를 안한 사람', bg='#ffffff', fg='#3F90CA',
                                    font=("Arial 18 bold"))
        did_not_start_mypc.place(x=175, y=100)

        self.trv.place(x=200,y=170)

        vsb = ttk.Scrollbar(self.window, orient="vertical", command=self.trv.yview)
        vsb.place(x=200 + 200 + 2, y=170, height=410 + 20)

        self.trv.configure(yscrollcommand=vsb.set)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial 15 bold"))
        style.configure("Treeview", rowheight=40)
        style.configure("Treeview", background="#3F90CA")

        self.trv.tag_configure('style',font=("Arial 15"))

        self.trv.column("#1", width=200, anchor="center")
        self.trv.heading(1, text='학번', anchor="center")

        back_image = PhotoImage(file='../image/back_icon.png')
        back_click = Button(borderwidth=0, command=self.go_back, bg='#ffffff', activebackground='#ffffff')
        back_click.place(x=40, y=20, anchor='nw')
        back_click.config(image=back_image)

        gagamel_image = PhotoImage(file='../image/smurf/gagamel_image.png')
        gagamel_label = Button(borderwidth=0, bg='#ffffff', activebackground='#ffffff')
        gagamel_label.place(x=530, y=100)
        gagamel_label.config(image=gagamel_image)

        self.window.mainloop()

    def update(self,rows) :
        self.trv.delete(*self.trv.get_children())
        for i in rows:
            self.trv.insert('', 'end', values=i, tag='style')

    #db connect
    def db_connect(self) :
        cal_time = CalTime()

        start_date = cal_time.start_date
        end_date = cal_time.end_date

        query = "SELECT hakbun, this_month from mypc_table"
        db_connect.cursor.execute(query)
        rows = db_connect.cursor.fetchall()

        submit_time_list = []

        for i in range(len(rows)):
            slice_year = int(rows[i][1][:4])
            slice_month = int(rows[i][1][5:7])
            slice_day = int(rows[i][1][8:10])
            slice_hour = int(rows[i][1][11:13])
            slice_minute = int(rows[i][1][14:])
            submit_time = datetime.datetime(slice_year, slice_month, slice_day, slice_hour, slice_minute)

            if start_date > submit_time or end_date < submit_time:
                submit_time_list.append(rows[i][0])

        self.update(submit_time_list)

    def go_back(self):
        from gui.teacher_menu import TeacherMenu
        self.window.destroy()
        TeacherMenu()
