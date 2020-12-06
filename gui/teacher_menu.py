from tkinter import *
from tkinter import messagebox as mb
import datetime
from DB.db_connect import DbConnect
from gui.did_not_start_mypc import DidNotStartMyPc
from gui.best_class_mypc import BestClassMypc
from gui.not_perfect_mypc import NotPerfectMypc


class TeacherMenu:
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#ffffff')
        self.window.resizable(False, False)

        did_not_start_image = PhotoImage(file='../image/did_not_start_btn.png')
        did_not_start_click = Button(borderwidth=0, command=self.go_did_not_start_page, bg='#ffffff', activebackground='#ffffff')
        did_not_start_click.place(x=50, y=180, anchor='nw')
        did_not_start_click.config(image=did_not_start_image)

        not_perfect_image = PhotoImage(file='../image/not_perfect_btn.png')
        not_perfect_click = Button(borderwidth=0, command=self.go_not_perfect_page, bg='#ffffff', activebackground='#ffffff')
        not_perfect_click.place(x=340, y=180, anchor='nw')
        not_perfect_click.config(image=not_perfect_image)

        best_class_image = PhotoImage(file='../image/best_class_btn.png')
        best_class_click = Button(borderwidth=0, command=self.go_best_class_page, bg='#ffffff', activebackground='#ffffff')
        best_class_click.place(x=705, y=180, anchor='nw')
        best_class_click.config(image=best_class_image)

        self.did_not_start_text = Label(text='내 PC 지키미를\n하지 않은 사람을\n볼 수 있습니다', bg='#ffffff', fg='#3F90CA', font=("Arial 18 bold"))
        self.did_not_start_text.place(x=75, y=400)

        self.not_perfect_text = Label(text='내 PC 지키미 점수가\n100점이 아닌 사람을\n볼 수 있습니다', bg='#ffffff', fg='#3F90CA', font=("Arial 18 bold"))
        self.not_perfect_text.place(x=385, y=400)

        self.best_class_text = Label(text='반별 내 PC 지키미\n점수 비율을\n볼 수 있습니다', bg='#ffffff', fg='#3F90CA', font=("Arial 18 bold"))
        self.best_class_text.place(x=725, y=400)

        back_image = PhotoImage(file='../image/back_icon.png')
        back_click = Button(borderwidth=0, command=self.go_start_page, bg='#ffffff', activebackground='#ffffff')
        back_click.place(x=40, y=20, anchor='nw')
        back_click.config(image=back_image)

        delete_image = PhotoImage(file='../image/delete_file.png')
        delete_btn = Button(borderwidth=0, command=self.delete_this_month_data, bg='#ffffff',
                                  activebackground='#ffffff')
        delete_btn.place(x=870, y=10, anchor='nw')
        delete_btn.config(image=delete_image)

        self.window.mainloop()

    def go_did_not_start_page(self):
        self.window.destroy()
        DidNotStartMyPc()

    def go_not_perfect_page(self):
        self.window.destroy()
        NotPerfectMypc()

    def go_best_class_page(self):
        self.window.destroy()
        BestClassMypc()

    def delete_this_month_data(self):
        res = mb.askquestion('저번 달 데이터 지우기','정말 저번 달 데이터를 지우시겠습니까?')
        if res == 'yes' :
            db_connect = DbConnect()
            this_month = "2020-" + str(datetime.datetime.now().month-1) + "%"
            query = "DELETE from mypc_table where this_month like %s"
            db_connect.cursor.execute(query, (this_month))
            db_connect.mydb.commit()
            mb.showinfo("데이터 삭제됨.","데이터가 성공적으로 삭제되었습니다!")
        else :
            return


    def go_start_page(self):
        from gui.start_page import StartPage
        self.window.destroy()
        StartPage()