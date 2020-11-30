from tkinter import *

class BestClassMypc:
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#272727')
        self.window.resizable(False, False)

        first_grade_image = PhotoImage(file='../image/first_grade_btn.png')
        first_grade_click = Button(borderwidth=0, command=self.go_first_grade_page, bg='#272727', activebackground='#272727')
        first_grade_click.place(x=60, y=200)
        first_grade_click.config(image=first_grade_image)

        second_grade_image = PhotoImage(file='../image/second_grade_btn.png')
        second_grade_click = Button(borderwidth=0, command=self.go_second_grade_page, bg='#272727', activebackground='#272727')
        second_grade_click.place(x=380, y=200)
        second_grade_click.config(image=second_grade_image)

        third_grade_image = PhotoImage(file='../image/third_grade_btn.png')
        third_grade_click = Button(borderwidth=0, command=self.go_third_grade_page, bg='#272727', activebackground='#272727')
        third_grade_click.place(x=700, y=200)
        third_grade_click.config(image=third_grade_image)

        self.window.mainloop()

    def go_first_grade_page(self):
        self.window.destroy()

    def go_second_grade_page(self):
        self.window.destroy()

    def go_third_grade_page(self):
        self.window.destroy()