from tkinter import *
from gui.student_menu import StudentMenu
from gui.teacher_menu import TeacherMenu

class StartPage:
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#272727')
        self.window.resizable(False, False)

        self.title = Label(text="IPC", bg='#272727', fg='#51F591', font=("Arial 60 bold"))
        self.explain = Label(text=": 앱설명앱설명앱설명앱설명앱설명앱설명앱설명앱설명", bg='#272727', fg='#51F591',
                        font=("System 13 normal"))
        self.title.place(x=140, y=180, anchor='nw')
        self.explain.place(x=140, y=270, anchor='nw')

        student_image = PhotoImage(file='../image/student_btn.png')
        student_click = Button(borderwidth=0, command=self.go_student_page, bg='#272727', activebackground='#272727')
        student_click.place(x=140, y=360)
        student_click.config(image=student_image)

        teacher_image = PhotoImage(file='../image/teacher_btn.png')
        teacher_click = Button(borderwidth=0, command=self.go_teacher_page, bg='#272727', activebackground='#272727')
        teacher_click.place(x=320, y=360)
        teacher_click.config(image=teacher_image)

        self.window.mainloop()

    def go_student_page(self):
        self.window.destroy()
        StudentMenu()

    def go_teacher_page(self):
        self.window.destroy()
        TeacherMenu()