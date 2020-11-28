from tkinter import *

class SearchIp:
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#272727')
        self.window.resizable(False, False)

        self.question = Label(text="학번을 입력하세요(ex.1101)", bg='#272727', fg='#51F591', font=("Arial 18 bold"))
        self.question.place(x=125, y=50)

        self.colon = Label(text=":", bg='#272727', fg='#51F591', font=("Arial 18 bold"))
        self.colon.place(x=125, y=90)

        search_btn_image = PhotoImage(file='../image/search_btn.png')
        search_btn_click = Button(borderwidth=0, command=self.search, bg='#272727', activebackground='#272727')
        search_btn_click.place(x=805, y=50)
        search_btn_click.config(image=search_btn_image)

        ip_box_image = PhotoImage(file='../image/ip_box.png')
        ip_box_click = Button(borderwidth=0, command=self.search, bg='#272727', activebackground='#272727')
        ip_box_click.place(x=125, y=180)
        ip_box_click.config(image=ip_box_image)

        use_whether_box_image = PhotoImage(file='../image/use_whether_box.png')
        use_whether_box_click = Button(borderwidth=0, command=self.search, bg='#272727', activebackground='#272727')
        use_whether_box_click.place(x=125, y=500)
        use_whether_box_click.config(image=use_whether_box_image)

        self.window.mainloop()

    def search(self):
        pass