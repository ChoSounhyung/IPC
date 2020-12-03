from tkinter import *
import pymysql
import datetime

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

this_year = datetime.datetime.today().year
this_month = datetime.datetime.today().month
first_index = datetime.date(this_year, this_month, 1).weekday()  # 매달 1일의 인덱스
minus = (3 - first_index) + 15

date = datetime.datetime(this_year, this_month, minus, 16, 30, 0)
pre_date = datetime.datetime(this_year, this_month, minus, 0, 0, 0)
print(pre_date)

class ThirdGradePage:
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#ffffff')
        self.window.resizable(False, False)

        self.mypc_text = Label(text='[3학년] 이달의 우수반', bg='#ffffff', fg='#3F90CA', font=("Arial 18 bold"))
        self.mypc_text.place(x=390, y=50)

        class_1, class_2, class_3, class_4, class_5, class_6 = self.db_connect()

        a = [int(class_1), int(class_2), int(class_3), int(class_4), int(class_5), int(class_6)]

        x = [1, 2, 3, 4, 5, 6]
        y = [a[0], a[1], a[2], a[3], a[4], a[5]]
        plt.bar(x, y, color='#FF6347')
        fig = plt.figure(1)

        canvas = FigureCanvasTkAgg(fig, self.window)
        canvas.draw()
        canvas.get_tk_widget().place(x=180, y=120)

        print(y)

        back_image = PhotoImage(file='../image/back_icon.png')
        back_click = Button(borderwidth=0, command=self.go_menu, bg='#ffffff', activebackground='#ffffff')
        back_click.place(x=40, y=20, anchor='nw')
        back_click.config(image=back_image)

        self.window.mainloop()

    def db_connect(self):
        mydb = pymysql.connect(host="localhost", user="root", password="123456", db="ipc")
        cursor = mydb.cursor()

        query = "SELECT this_month from mypc_table where hakbun like '31%'"
        cursor.execute(query)
        rows = cursor.fetchall()

        time_sum = 0

        for i in range(len(rows)):
            slice_year = int(rows[i][0][:4])
            slice_month = int(rows[i][0][5:7])
            slice_day = int(rows[i][0][8:10])
            slice_hour = int(rows[i][0][11:13])
            slice_minute = int(rows[i][0][14:])
            submit_time = datetime.datetime(slice_year, slice_month, slice_day, slice_hour, slice_minute)

            if pre_date <= submit_time:
                time_sum += round((date - submit_time).microseconds / float(1000000)) + (
                        (date - submit_time).seconds + (date - submit_time).days * 24 * 3600)

        avg = time_sum // 720
        class_1 = str(avg)

        query = "SELECT this_month from mypc_table where hakbun like '32%'"
        cursor.execute(query)
        rows = cursor.fetchall()

        time_sum = 0

        for i in range(len(rows)):
            slice_year = int(rows[i][0][:4])
            slice_month = int(rows[i][0][5:7])
            slice_day = int(rows[i][0][8:10])
            slice_hour = int(rows[i][0][11:13])
            slice_minute = int(rows[i][0][14:])
            submit_time = datetime.datetime(slice_year, slice_month, slice_day, slice_hour, slice_minute)

            if pre_date <= submit_time:
                time_sum += round((date - submit_time).microseconds / float(1000000)) + (
                        (date - submit_time).seconds + (date - submit_time).days * 24 * 3600)

        avg = time_sum // 720
        class_2 = str(avg)

        query = "SELECT this_month from mypc_table where hakbun like '33%'"
        cursor.execute(query)
        rows = cursor.fetchall()

        time_sum = 0

        for i in range(len(rows)):
            slice_year = int(rows[i][0][:4])
            slice_month = int(rows[i][0][5:7])
            slice_day = int(rows[i][0][8:10])
            slice_hour = int(rows[i][0][11:13])
            slice_minute = int(rows[i][0][14:])
            submit_time = datetime.datetime(slice_year, slice_month, slice_day, slice_hour, slice_minute)

            if pre_date <= submit_time:
                time_sum += round((date - submit_time).microseconds / float(1000000)) + (
                        (date - submit_time).seconds + (date - submit_time).days * 24 * 3600)

        avg = time_sum // 720
        class_3 = str(avg)

        query = "SELECT this_month from mypc_table where hakbun like '34%'"
        cursor.execute(query)
        rows = cursor.fetchall()

        time_sum = 0

        for i in range(len(rows)):
            slice_year = int(rows[i][0][:4])
            slice_month = int(rows[i][0][5:7])
            slice_day = int(rows[i][0][8:10])
            slice_hour = int(rows[i][0][11:13])
            slice_minute = int(rows[i][0][14:])
            submit_time = datetime.datetime(slice_year, slice_month, slice_day, slice_hour, slice_minute)

            if pre_date <= submit_time:
                time_sum += round((date - submit_time).microseconds / float(1000000)) + (
                        (date - submit_time).seconds + (date - submit_time).days * 24 * 3600)

        avg = time_sum // 720
        class_4 = str(avg)

        query = "SELECT this_month from mypc_table where hakbun like '35%'"
        cursor.execute(query)
        rows = cursor.fetchall()

        time_sum = 0

        for i in range(len(rows)):
            slice_year = int(rows[i][0][:4])
            slice_month = int(rows[i][0][5:7])
            slice_day = int(rows[i][0][8:10])
            slice_hour = int(rows[i][0][11:13])
            slice_minute = int(rows[i][0][14:])
            submit_time = datetime.datetime(slice_year, slice_month, slice_day, slice_hour, slice_minute)

            if pre_date <= submit_time:
                time_sum += round((date - submit_time).microseconds / float(1000000)) + (
                        (date - submit_time).seconds + (date - submit_time).days * 24 * 3600)

        avg = time_sum // 720
        class_5 = str(avg)

        query = "SELECT this_month from mypc_table where hakbun like '36%'"
        cursor.execute(query)
        rows = cursor.fetchall()

        time_sum = 0

        for i in range(len(rows)):
            slice_year = int(rows[i][0][:4])
            slice_month = int(rows[i][0][5:7])
            slice_day = int(rows[i][0][8:10])
            slice_hour = int(rows[i][0][11:13])
            slice_minute = int(rows[i][0][14:])
            submit_time = datetime.datetime(slice_year, slice_month, slice_day, slice_hour, slice_minute)

            if pre_date <= submit_time:
                time_sum += round((date - submit_time).microseconds / float(1000000)) + (
                        (date - submit_time).seconds + (date - submit_time).days * 24 * 3600)
                print(round((date - submit_time).microseconds / float(1000000)) + (
                        (date - submit_time).seconds + (date - submit_time).days * 24 * 3600))

        avg = time_sum // 720
        class_6 = str(avg)

        return class_1, class_2, class_3, class_4, class_5, class_6

    def go_menu(self):
        from gui.best_class_mypc import BestClassMypc
        self.window.destroy()
        BestClassMypc()