from tkinter import *
import pymysql

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

class ThirdGradePage:
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#272727')
        self.window.resizable(False, False)

        self.mypc_text = Label(text='[3학년] 이달의 우수반', bg='#272727', fg='#ffffff', font=("Arial 18 bold"))
        self.mypc_text.place(x=390, y=50)

        class_1, class_2, class_3, class_4, class_5, class_6 = self.db_connect()

        x = ['1반', '2반', '3반', '4반', '5반', '6반']
        y = [class_1, class_2, class_3, class_4, class_5, class_6]
        plt.bar(x, y, color='#FFA500')
        fig = plt.figure(1)

        canvas = FigureCanvasTkAgg(fig, self.window)
        canvas.draw()
        canvas.get_tk_widget().place(x=180, y=120)

        self.window.mainloop()

    def db_connect(self):
        mydb = pymysql.connect(host="localhost", user="root", password="s2019w36", db="ipc")
        cursor = mydb.cursor()

        query = "SELECT count(*) from mypc_table where hakbun like '31%' and score=100"
        cursor.execute(query)
        rows = cursor.fetchall()
        class_1 = (rows[0][0])

        query = "SELECT count(*) from mypc_table where hakbun like '32%' and score=100"
        cursor.execute(query)
        rows = cursor.fetchall()
        class_2 = (rows[0][0])

        query = "SELECT count(*) from mypc_table where hakbun like '33%' and score=100"
        cursor.execute(query)
        rows = cursor.fetchall()
        class_3 = (rows[0][0])

        query = "SELECT count(*) from mypc_table where hakbun like '34%' and score=100"
        cursor.execute(query)
        rows = cursor.fetchall()
        class_4 = (rows[0][0])

        query = "SELECT count(*) from mypc_table where hakbun like '35%' and score=100"
        cursor.execute(query)
        rows = cursor.fetchall()
        class_5 = (rows[0][0])

        query = "SELECT count(*) from mypc_table where hakbun like '36%' and score=100"
        cursor.execute(query)
        rows = cursor.fetchall()
        class_6 = (rows[0][0])

        return class_1, class_2, class_3, class_4, class_5, class_6