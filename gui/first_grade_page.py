from tkinter import *
import pymysql

import pandas as pd
import numpy as np

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

        class_1, class_2, class_3, class_4, class_5, class_6 = self.db_connect()

        x = ['1반', '2반', '3반', '4반', '5반', '6반']
        y = [class_1, class_2, class_3, class_4, class_5, class_6]
        plt.bar(x, y)
        plt.show()
        plt.gcf().canvas.draw()
        fig = plt.figure()
        canvas = FigureCanvasTkAgg(fig, self.window)
        canvas.get_tk_widget().grid(row=1, column=6)
        canvas.get_tk_widget().pack()

        # canvas = FigureCanvasTkAgg(fig, self.window)  #
        # canvas.get_tk_widget().grid(column=0, row=1)  #

        self.window.mainloop()


    def db_connect(self):
        mydb = pymysql.connect(host="localhost", user="root", password="s2019w36", db="ipc")
        cursor = mydb.cursor()

        query = "SELECT count(*) from mypc_table where hakbun like '11%' and score=100"
        cursor.execute(query)
        rows = cursor.fetchall()
        class_1 = (rows[0][0])

        query = "SELECT count(*) from mypc_table where hakbun like '12%' and score=100"
        cursor.execute(query)
        rows = cursor.fetchall()
        class_2 = (rows[0][0])

        query = "SELECT count(*) from mypc_table where hakbun like '13%' and score=100"
        cursor.execute(query)
        rows = cursor.fetchall()
        class_3 = (rows[0][0])

        query = "SELECT count(*) from mypc_table where hakbun like '14%' and score=100"
        cursor.execute(query)
        rows = cursor.fetchall()
        class_4 = (rows[0][0])

        query = "SELECT count(*) from mypc_table where hakbun like '15%' and score=100"
        cursor.execute(query)
        rows = cursor.fetchall()
        class_5 = (rows[0][0])

        query = "SELECT count(*) from mypc_table where hakbun like '16%' and score=100"
        cursor.execute(query)
        rows = cursor.fetchall()
        class_6 = (rows[0][0])

        return class_1, class_2, class_3, class_4, class_5, class_6