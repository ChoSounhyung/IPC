from tkinter import *

class MyPc:
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#272727')
        self.window.resizable(False, False)

        self.this_month_text = Label(text='This Month', bg='#272727', fg='#F6D875', font=("Arial 18 bold"))
        self.this_month_text.place(x=80, y=50)

        self.input_classof = Label(text='학번을 입력하세요(ex.1101)', bg='#272727', fg='#51F591', font=("Arial 18 bold"))
        self.input_classof.place(x=80, y=200)

        self.input_score = Label(text='점수를 입력하세요(ex.100)', bg='#272727', fg='#51F591', font=("Arial 18 bold"))
        self.input_score.place(x=450, y=200)

        submit_btn_image = PhotoImage(file='../image/submit_btn.png')
        submit_btn_click = Button(borderwidth=0, command=self.submit, bg='#272727', activebackground='#272727')
        submit_btn_click.place(x=800, y=200)
        submit_btn_click.config(image=submit_btn_image)

        self.window.mainloop()

    def submit(self):
        pass