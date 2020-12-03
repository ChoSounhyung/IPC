from tkinter import *
from model.cal_time import CalTime

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from DB.db_connect import DbConnect

db_connect = DbConnect()

class SecondGradePage:
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#ffffff')
        self.window.resizable(False, False)

        self.mypc_text = Label(text='[2학년] 이달의 우수반', bg='#ffffff', fg='#3F90CA', font=("Arial 18 bold"))
        self.mypc_text.place(x=390, y=50)

        class_1, class_2, class_3, class_4, class_5, class_6 = self.db_connect()

        x = [1, 2, 3, 4, 5, 6]
        y = [int(class_1), int(class_2), int(class_3), int(class_4), int(class_5), int(class_6)]

        plt.bar(x, y, color='#F8A9A9')
        fig = plt.figure(1)

        canvas = FigureCanvasTkAgg(fig, self.window)
        canvas.draw()
        canvas.get_tk_widget().place(x=180, y=120)

        print(y)

        back_image = PhotoImage(file='../image/back_icon.png')
        back_click = Button(borderwidth=0, command=self.go_menu, bg='#ffffff', activebackground='#ffffff')
        back_click.place(x=40, y=20, anchor='nw')
        back_click.config(image=back_image)

        if ''.join(str(y)) != "000000":
            for i in range(len(y)):
                if y[i] == max(y) and y[i] != 0:
                    self.search_ip_text = Label(text=str(i + 1) + "반이 기한내에 가장 빨리 제출했습니다.", bg='#ffffff', fg='#3F90CA',
                                                font=("Arial 18 bold"))
                    self.search_ip_text.place(x=300, y=100)

        self.window.mainloop()

    def db_connect(self):
        cal_time = CalTime()

        query = "SELECT this_month from mypc_table where hakbun like '21%'"
        class_1 = cal_time.calculate(query)

        query = "SELECT this_month from mypc_table where hakbun like '22%'"
        class_2 = cal_time.calculate(query)

        query = "SELECT this_month from mypc_table where hakbun like '23%'"
        class_3 = cal_time.calculate(query)

        query = "SELECT this_month from mypc_table where hakbun like '24%'"
        class_4 = cal_time.calculate(query)

        query = "SELECT this_month from mypc_table where hakbun like '25%'"
        class_5 = cal_time.calculate(query)

        query = "SELECT this_month from mypc_table where hakbun like '26%'"
        class_6 = cal_time.calculate(query)

        return class_1, class_2, class_3, class_4, class_5, class_6

    def go_menu(self):
        from gui.best_class_mypc import BestClassMypc
        self.window.destroy()
        BestClassMypc()