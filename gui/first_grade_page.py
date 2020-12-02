from tkinter import *
import pymysql
import datetime

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

class FirstGradePage:
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#272727')
        self.window.resizable(False, False)

        self.mypc_text = Label(text='[1학년] 이달의 우수반', bg='#272727', fg='#ffffff', font=("Arial 18 bold"))
        self.mypc_text.place(x=390, y=50)

        class_1, class_2, class_3, class_4, class_5, class_6 = self.db_connect()

        x = ['1반', '2반', '3반', '4반', '5반', '6반']
        y = [class_1, class_2, class_3, class_4, class_5, class_6]
        plt.bar(x, y, color='#FF6347')
        fig = plt.figure(1)

        canvas = FigureCanvasTkAgg(fig, self.window)
        canvas.draw()
        canvas.get_tk_widget().place(x=180, y=120)

        print(y)

        self.window.mainloop()

    def db_connect(self):
        mydb = pymysql.connect(host="localhost", user="root", password="s2019w36", db="ipc")
        cursor = mydb.cursor()

        query = "SELECT this_month from mypc_table where hakbun like '11%'"
        cursor.execute(query)
        rows = cursor.fetchall()

        this_year = str(datetime.datetime.today().year)
        this_month = str(datetime.datetime.today().month)
        first_index = datetime.date(int(this_year), int(this_month), 1).weekday()  # 매달 1일의 인덱스
        minus = str((3 - first_index) + 15)
        dead_line = this_year+"-"+this_month+"-"+minus+" 16:30"

        date = datetime.datetime.strptime(dead_line, "%Y-%m-%d %H:%M")

        count = 0

        for i in range(len(rows)):
            submit_time = datetime.datetime.strptime(rows[i][0], "%Y-%m-%d %H:%M")
            if submit_time < date:
                count += 1

        class_1 = count
        print(class_1)

        query = "SELECT this_month from mypc_table where hakbun like '12%'"
        cursor.execute(query)
        rows = cursor.fetchall()

        this_year = str(datetime.datetime.today().year)
        this_month = str(datetime.datetime.today().month)
        first_index = datetime.date(int(this_year), int(this_month), 1).weekday()  # 매달 1일의 인덱스
        minus = str((3 - first_index) + 15)
        dead_line = this_year + "-" + this_month + "-" + minus + " 16:30"

        date = datetime.datetime.strptime(dead_line, "%Y-%m-%d %H:%M")

        count = 0

        for i in range(len(rows)):
            submit_time = datetime.datetime.strptime(rows[i][0], "%Y-%m-%d %H:%M")
            if submit_time < date:
                count += 1

        class_2 = count
        print(class_2)

        query = "SELECT this_month from mypc_table where hakbun like '13%'"
        cursor.execute(query)
        rows = cursor.fetchall()

        this_year = str(datetime.datetime.today().year)
        this_month = str(datetime.datetime.today().month)
        first_index = datetime.date(int(this_year), int(this_month), 1).weekday()  # 매달 1일의 인덱스
        minus = str((3 - first_index) + 15)
        dead_line = this_year + "-" + this_month + "-" + minus + " 16:30"

        date = datetime.datetime.strptime(dead_line, "%Y-%m-%d %H:%M")

        count = 0

        for i in range(len(rows)):
            submit_time = datetime.datetime.strptime(rows[i][0], "%Y-%m-%d %H:%M")
            if submit_time < date:
                count += 1

        class_3 = count
        print(class_3)

        query = "SELECT this_month from mypc_table where hakbun like '14%'"
        cursor.execute(query)
        rows = cursor.fetchall()

        this_year = str(datetime.datetime.today().year)
        this_month = str(datetime.datetime.today().month)
        first_index = datetime.date(int(this_year), int(this_month), 1).weekday()  # 매달 1일의 인덱스
        minus = str((3 - first_index) + 15)
        dead_line = this_year + "-" + this_month + "-" + minus + " 16:30"

        date = datetime.datetime.strptime(dead_line, "%Y-%m-%d %H:%M")

        count = 0

        for i in range(len(rows)):
            submit_time = datetime.datetime.strptime(rows[i][0], "%Y-%m-%d %H:%M")
            if submit_time < date:
                count += 1

        class_4 = count
        print(class_4)

        query = "SELECT this_month from mypc_table where hakbun like '15%'"
        cursor.execute(query)
        rows = cursor.fetchall()

        this_year = str(datetime.datetime.today().year)
        this_month = str(datetime.datetime.today().month)
        first_index = datetime.date(int(this_year), int(this_month), 1).weekday()  # 매달 1일의 인덱스
        minus = str((3 - first_index) + 15)
        dead_line = this_year + "-" + this_month + "-" + minus + " 16:30"

        date = datetime.datetime.strptime(dead_line, "%Y-%m-%d %H:%M")

        count = 0

        for i in range(len(rows)):
            submit_time = datetime.datetime.strptime(rows[i][0], "%Y-%m-%d %H:%M")
            if submit_time < date:
                count += 1

        class_5 = count
        print(class_5)

        query = "SELECT this_month from mypc_table where hakbun like '16%'"
        cursor.execute(query)
        rows = cursor.fetchall()

        this_year = str(datetime.datetime.today().year)
        this_month = str(datetime.datetime.today().month)
        first_index = datetime.date(int(this_year), int(this_month), 1).weekday()  # 매달 1일의 인덱스
        minus = str((3 - first_index) + 15)
        dead_line = this_year + "-" + this_month + "-" + minus + " 16:30"

        date = datetime.datetime.strptime(dead_line, "%Y-%m-%d %H:%M")

        count = 0

        for i in range(len(rows)):
            submit_time = datetime.datetime.strptime(rows[i][0], "%Y-%m-%d %H:%M")
            if submit_time < date:
                count += 1

        class_6 = count
        print(class_6)

        return class_1, class_2, class_3, class_4, class_5, class_6