from tkinter import *
from gui.search_ip_page import SearchIp
#from gui.start_page import StartPage
from gui.mypc_page import MyPc

class StudentPage:
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#272727')
        self.window.resizable(False, False)

        search_ip_image = PhotoImage(file='../image/search_ip_btn.png')
        search_ip_click = Button(borderwidth=0, command=self.go_search_ip_page, bg='#272727', activebackground='#272727')
        search_ip_click.place(x=140, y=150, anchor='nw')
        search_ip_click.config(image=search_ip_image)

        mypc_image = PhotoImage(file='../image/mypc_prot_btn.png')
        mypc_click = Button(borderwidth=0, command=self.go_mypc_page, bg='#272727', activebackground='#272727')
        mypc_click.place(x=540, y=150, anchor='nw')
        mypc_click.config(image=mypc_image)

        self.search_ip_text = Label(text='학번을 입력하면\nIP 주소와 IP 사용여부를\n알 수 있습니다', bg='#272727', fg='#51F591', font=("Arial 18 bold"))
        self.search_ip_text.place(x=170, y=400)

        self.mypc_text = Label(text='내 PC 지키미 점수를 입력해\n선생님께 제출합니다', bg='#272727', fg='#51F591', font=("Arial 18 bold"))
        self.mypc_text.place(x=555, y=400)

        # home_image = PhotoImage(file='../image/home_btn.png')
        # home_click = Button(borderwidth=0, command=self.go_start_page, bg='#272727', activebackground='#272727')
        # home_click.place(x=50, y=600, anchor='nw')
        # home_click.config(image=home_image)

        self.window.mainloop()

    def go_search_ip_page(self):
        self.window.destroy()
        SearchIp()

    def go_mypc_page(self):
        self.window.destroy()
        MyPc()

    # def go_start_page(self):
    #     self.window.destroy()
    #     StartPage