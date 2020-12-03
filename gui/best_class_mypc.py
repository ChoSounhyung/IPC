from tkinter import *
from gui.first_grade_page import FirstGradePage
from gui.second_grade_page import SecondGradePage
from gui.third_grade_page import ThirdGradePage

class BestClassMypc:
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#ffffff')
        self.window.resizable(False, False)

        first_grade_image = PhotoImage(file='../image/first_grade_btn.png')
        first_grade_click = Button(borderwidth=0, command=self.go_first_grade_page, bg='#ffffff', activebackground='#ffffff')
        first_grade_click.place(x=60, y=100)
        first_grade_click.config(image=first_grade_image)

        second_grade_image = PhotoImage(file='../image/second_grade_btn.png')
        second_grade_click = Button(borderwidth=0, command=self.go_second_grade_page, bg='#ffffff', activebackground='#ffffff')
        second_grade_click.place(x=380, y=100)
        second_grade_click.config(image=second_grade_image)

        third_grade_image = PhotoImage(file='../image/third_grade_btn.png')
        third_grade_click = Button(borderwidth=0, command=self.go_third_grade_page, bg='#ffffff', activebackground='#ffffff')
        third_grade_click.place(x=700, y=100)
        third_grade_click.config(image=third_grade_image)

        back_image = PhotoImage(file='../image/back_icon.png')
        back_click = Button(borderwidth=0, command=self.go_back, bg='#ffffff', activebackground='#ffffff')
        back_click.place(x=40, y=20, anchor='nw')
        back_click.config(image=back_image)

        first_smurf_image = PhotoImage(file='../image/smurf/first_smurf.png')
        first_smurf_label = Button(borderwidth=0, bg='#ffffff', activebackground='#ffffff')
        first_smurf_label.place(x=45, y=280)
        first_smurf_label.config(image=first_smurf_image)

        second_smurf_image = PhotoImage(file='../image/smurf/second_smurf.png')
        second_smurf_label = Button(borderwidth=0, bg='#ffffff', activebackground='#ffffff')
        second_smurf_label.place(x=340, y=280)
        second_smurf_label.config(image=second_smurf_image)

        third_smurf_image = PhotoImage(file='../image/smurf/third_smurf.png')
        third_smurf_label = Button(borderwidth=0, bg='#ffffff', activebackground='#ffffff')
        third_smurf_label.place(x=680, y=280)
        third_smurf_label.config(image=third_smurf_image)

        self.window.mainloop()

    def go_first_grade_page(self):
        self.window.destroy()
        FirstGradePage()

    def go_second_grade_page(self):
        self.window.destroy()
        SecondGradePage()

    def go_third_grade_page(self):
        self.window.destroy()
        ThirdGradePage()

    def go_back(self):
        from gui.teacher_menu import TeacherMenu
        self.window.destroy()
        TeacherMenu()