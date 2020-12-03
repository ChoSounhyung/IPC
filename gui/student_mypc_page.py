from tkinter import *
from tkinter import messagebox
import tkinter as tk
import datetime

from DB.db_connect import DbConnect

db_connect = DbConnect()

class MyPc:
    def __init__(self):
        pass

    def cleanup(self,new_hakbun, new_score, result):
        reason = self.e.get()
        print(reason)
        self.popup.destroy()

        now = datetime.datetime.now()
        this_month = now.strftime('%Y-%m-%d %H:%M')

        if (result == 0):  # 데이터가 존재하지 않을 때 - insert
            query = "insert into mypc_table values(%s,%s,%s,%s)"
            db_connect.cursor.execute(query, (new_hakbun, this_month, new_score, reason))
            db_connect.mydb.commit()
            student_query = "UPDATE student_table SET check_mypc= %s where hakbun = %s"
            db_connect.cursor.execute(student_query,("O",new_hakbun))
            db_connect.mydb.commit()
        else:  # 데이터가 존재할 때 - update
            query = "UPDATE mypc_table SET score=%s where hakbun = %s"
            DbConnect.cursor.execute(query, (new_score, new_hakbun))
            #이유 업데이트
            query = "UPDATE mypc_table SET reason=%s where hakbun = %s"
            db_connect.cursor.execute(query, (reason, new_hakbun))
            query = "UPDATE mypc_table set this_month = %s where hakbun = %s"
            db_connect.cursor.execute(query,(this_month,new_hakbun))
            db_connect.mydb.commit()

        self.info()

    def submit(self):
        new_hakbun = self.in_new_h.get()
        new_score = int(self.in_new_s.get())
        print(new_hakbun,new_score)
        query = "select exists (select * from mypc_table where hakbun=%s) as success"

        db_connect.cursor.execute(query, (new_hakbun))
        rows = DbConnect.cursor.fetchall()
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
                db_connect.cursor.execute(query, (new_hakbun, this_month, new_score, reason))
                db_connect.mydb.commit()
                student_query = "UPDATE student_table SET check_mypc= %s where hakbun = %s"
                db_connect.cursor.execute(student_query,("O",new_hakbun))
                db_connect.mydb.commit()

            else:  # 데이터가 존재할 때 - update
                query = "UPDATE mypc_table SET score=%s where hakbun = %s"
                db_connect.cursor.execute(query, (new_score, new_hakbun))
                #이유 업데이트
                query = "UPDATE mypc_table SET reason=%s where hakbun = %s"
                db_connect.cursor.execute(query, (reason, new_hakbun))
                query = "UPDATE mypc_table set this_month = %s where hakbun = %s"
                db_connect.cursor.execute(query,(this_month,new_hakbun))
                db_connect.mydb.commit()

            self.info()

    def show_row(self, this_month, hakbun, score, reason):
        if(reason=="empty") :
            self.new_row.set(f'{this_month}\t    {hakbun}\t    {score}')
        else :
            self.new_row.set(f'{this_month}\t    {hakbun}\t    {score}\t    {reason}')

    def search(self):
        self.warning()

        hakbun = self.new_h.get()
        query = "select this_month,hakbun,score,reason from mypc_table where hakbun=%s"
        try :
            db_connect.cursor.execute(query, (hakbun))
            rows = DbConnect.cursor.fetchall()
            data_list = list(rows[0])
            #데이터 분할
            this_month = data_list[0]
            hakbun = data_list[1]
            score = data_list[2]
            reason = data_list[3]
            self.show_row(this_month, hakbun, score, reason)
        except :
            self.show_row("해당하는 데이터가 없습니다.", "", "", "")


    def info(self):
        tk.messagebox.showinfo("info", "  제출되었습니다!\t")

    def warning(self):
        tk.messagebox.showwarning("warning", "3초만 기다려주세요!")
