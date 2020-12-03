from tkinter import *
from tkinter import messagebox
import pymysql
import tkinter as tk
import datetime

class MyPc:
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#ffffff')
        self.window.resizable(False, False)
        self.new_h = StringVar()
        self.new_row = StringVar()
        self.in_new_h = StringVar()
        self.in_new_s = StringVar()
        self.value = StringVar()

        self.question = Label(text="학번을 입력하세요(ex.1101)", bg='#ffffff', fg='#3F90CA', font=("Arial 18 bold"))
        self.question.place(x=80, y=100)

        self.ent = Entry(bg='#ffffff', fg='#3F90CA', font=("Arial 18 bold"), textvariable=self.new_h)
        self.ent.place(x=80, y=140)

        search_btn_image = PhotoImage(file='../image/search_btn.png')
        search_btn_click = Button(borderwidth=0, command=self.search, bg='#ffffff', activebackground='#ffffff')
        search_btn_click.place(x=805, y=100)
        search_btn_click.config(image=search_btn_image)

        self.this_month_text = Label(text='제출시간\t\t    학번\t    점수\t    이유', bg='#ffffff', fg='#F6D875', font=("Arial 18 bold"))
        self.this_month_text.place(x=80, y=250)

        #new row
        self.this_month_change = Label(textvariable=self.new_row, bg='#ffffff', fg='#F6D875', font=("Arial 18 bold"))
        self.this_month_change.place(x=80, y=280)


        self.input_classof = Label(text='학번을 입력하세요(ex.1101)', bg='#ffffff', fg='#3F90CA', font=("Arial 18 bold"))
        self.input_classof.place(x=80, y=400)

        #insert hakbun
        self.classof_ent = Entry(bg='#ffffff', fg='#3F90CA', font=("Arial 18 bold"), textvariable=self.in_new_h)
        self.classof_ent.place(x=80, y=440)

        self.input_score = Label(text='점수를 입력하세요(ex.100)', bg='#ffffff', fg='#3F90CA', font=("Arial 18 bold"))
        self.input_score.place(x=450, y=400)

        #insert score
        self.score_ent = Entry(bg='#ffffff', fg='#3F90CA', font=("Arial 18 bold"), textvariable=self.in_new_s)
        self.score_ent.place(x=450, y=440)

        submit_btn_image = PhotoImage(file='../image/submit_btn.png')
        submit_btn_click = Button(borderwidth=0, command=self.submit, bg='#ffffff', activebackground='#ffffff')
        submit_btn_click.place(x=800, y=400)
        submit_btn_click.config(image=submit_btn_image)

        back_image = PhotoImage(file='../image/back_icon.png')
        back_click = Button(borderwidth=0, command=self.go_back, bg='#ffffff', activebackground='#ffffff')
        back_click.place(x=40, y=20, anchor='nw')
        back_click.config(image=back_image)

        self.window.mainloop()

    def cleanup(self,new_hakbun, new_score, result):
        reason = self.e.get()
        print(reason)
        self.popup.destroy()

        mydb = pymysql.connect(host="localhost", user="root", password="123456", db="ipc")
        cursor = mydb.cursor()

        now = datetime.datetime.now()
        this_month = now.strftime('%Y-%m-%d %H:%M')

        if (result == 0):  # 데이터가 존재하지 않을 때 - insert
            query = "insert into mypc_table values(%s,%s,%s,%s)"
            cursor.execute(query, (new_hakbun, this_month, new_score, reason))
            mydb.commit()
            student_query = "UPDATE student_table SET check_mypc= %s where hakbun = %s"
            cursor.execute(student_query,("O",new_hakbun))
            mydb.commit()
        else:  # 데이터가 존재할 때 - update
            query = "UPDATE mypc_table SET score=%s where hakbun = %s"
            cursor.execute(query, (new_score, new_hakbun))
            #이유 업데이트
            query = "UPDATE mypc_table SET reason=%s where hakbun = %s"
            cursor.execute(query, (reason, new_hakbun))
            query = "UPDATE mypc_table set this_month = %s where hakbun = %s"
            cursor.execute(query,(this_month,new_hakbun))
            mydb.commit()

        self.info()

    def submit(self):
        mydb = pymysql.connect(host="localhost", user="root", password="123456", db="ipc")
        cursor = mydb.cursor()
        new_hakbun = self.in_new_h.get()
        new_score = int(self.in_new_s.get())
        print(new_hakbun,new_score)
        query = "select exists (select * from mypc_table where hakbun=%s) as success"

        cursor.execute(query, (new_hakbun))
        rows = cursor.fetchall()
        data_list = list(rows[0])
        # 데이터 분할
        result = data_list[0]
        #이번 달 구하기
        now = datetime.datetime.now()
        this_month = now.strftime('%Y-%m-%d %H:%M')
        reason = ""
        if(new_score<100) :

            self.popup = Tk()
            self.popup.title("이유를 입력하세요.")
            self.popup.geometry("300x150+620+320")
            self.popup.config(bg='#ffffff')
            #self.popup.resizable(False, False)

            self.l = Label(self.popup, text="이유를 입력하세요.", bg="#ffffff", font=("Arial 10 bold"))
            self.l.place(x=90, y=35)
            self.e = Entry(self.popup, bg="#E5E5E5", textvariable=self.value, width=27)
            self.e.insert(0, '이유를 입력하세요')
            self.e.place(x=30, y=80)
            self.b = Button(self.popup, text="등록", command=lambda : self.cleanup(new_hakbun, new_score, result))
            self.b.place(x=235, y=75)
            #print(self.value.get())
            self.popup.mainloop()

        else :
            reason = "empty"
            print(reason,result)
            if (result == 0):  # 데이터가 존재하지 않을 때 - insert
                query = "insert into mypc_table values(%s,%s,%s,%s)"
                cursor.execute(query, (new_hakbun, this_month, new_score, reason))
                mydb.commit()
                student_query = "UPDATE student_table SET check_mypc= %s where hakbun = %s"
                cursor.execute(student_query,("O",new_hakbun))
                mydb.commit()

            else:  # 데이터가 존재할 때 - update
                query = "UPDATE mypc_table SET score=%s where hakbun = %s"
                cursor.execute(query, (new_score, new_hakbun))
                #이유 업데이트
                query = "UPDATE mypc_table SET reason=%s where hakbun = %s"
                cursor.execute(query, (reason, new_hakbun))
                query = "UPDATE mypc_table set this_month = %s where hakbun = %s"
                cursor.execute(query,(this_month,new_hakbun))
                mydb.commit()

            self.info()



    def show_row(self, this_month, hakbun, score, reason):
        if(reason=="empty") :
            self.new_row.set(f'{this_month}\t    {hakbun}\t    {score}')
        else :
            self.new_row.set(f'{this_month}\t    {hakbun}\t    {score}\t    {reason}')

    def search(self):
        mydb = pymysql.connect(host="localhost", user="root", password="123456", db="ipc")
        cursor = mydb.cursor()
        hakbun = self.new_h.get()
        query = "select this_month,hakbun,score,reason from mypc_table where hakbun=%s"
        try :
            cursor.execute(query, (hakbun))
            rows = cursor.fetchall()
            data_list = list(rows[0])
            #데이터 분할
            this_month = data_list[0]
            hakbun = data_list[1]
            score = data_list[2]
            reason = data_list[3]
            self.show_row(this_month, hakbun, score, reason)
        except :
            self.show_row("해당하는 데이터가 없습니다.", "", "", "")

    def go_back(self):
        from gui.student_menu import StudentMenu
        self.window.destroy()
        StudentMenu()

    def info(self):
        tk.messagebox.showinfo("info", "  제출되었습니다!\t")
