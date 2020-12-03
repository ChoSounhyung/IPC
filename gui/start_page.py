from tkinter import *
from gui.student_menu import StudentMenu
from gui.teacher_menu import TeacherMenu

class StartPage:
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#ffffff')
        self.window.resizable(False, False)

        self.title = Label(text="IPC", bg='#ffffff', fg='#3F90CA', font=("Arial 60 bold"))
        self.explain = Label(text=": IP 검색과 내 PC 지키미 결과를 제출, 확인해보아요!", bg='#ffffff', fg='#3F90CA',
                        font=("System 13 normal"))
        self.title.place(x=110, y=180, anchor='nw')
        self.explain.place(x=110, y=270, anchor='nw')

        student_image = PhotoImage(file='../image/student_btn.png')
        student_click = Button(borderwidth=0, command=self.go_student_page, bg='#ffffff', activebackground='#ffffff')
        student_click.place(x=110, y=360)
        student_click.config(image=student_image)

        teacher_image = PhotoImage(file='../image/teacher_btn.png')
        teacher_click = Button(borderwidth=0, command=self.go_teacher_page, bg='#ffffff', activebackground='#ffffff')
        teacher_click.place(x=300, y=360)
        teacher_click.config(image=teacher_image)

        notebook_smurf_image = PhotoImage(file='../image/smurf/notebook_smurf.png')
        notebook_smurf_label = Button(borderwidth=0, bg='#ffffff', activebackground='#ffffff')
        notebook_smurf_label.place(x=570, y=100)
        notebook_smurf_label.config(image=notebook_smurf_image)

        self.window.mainloop()

    def go_student_page(self):
        self.window.destroy()
        StudentMenu()

    def go_teacher_page(self):
        self.window.destroy()
        TeacherMenu()