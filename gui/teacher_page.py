from tkinter import *

class TeacherPage:
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#272727')
        self.window.resizable(False, False)

        did_not_start_image = PhotoImage(file='../image/did_not_start_btn.png')
        did_not_start_click = Button(borderwidth=0, command=self.go_did_not_start_page, bg='#272727', activebackground='#272727')
        did_not_start_click.place(x=50, y=180, anchor='nw')
        did_not_start_click.config(image=did_not_start_image)

        not_perfect_image = PhotoImage(file='../image/not_perfect_btn.png')
        not_perfect_click = Button(borderwidth=0, command=self.go_not_perfect_page, bg='#272727', activebackground='#272727')
        not_perfect_click.place(x=340, y=180, anchor='nw')
        not_perfect_click.config(image=not_perfect_image)

        best_class_image = PhotoImage(file='../image/best_class_btn.png')
        best_class_click = Button(borderwidth=0, command=self.go_best_class_page, bg='#272727', activebackground='#272727')
        best_class_click.place(x=705, y=180, anchor='nw')
        best_class_click.config(image=best_class_image)

        self.window.mainloop()

    def go_did_not_start_page(self):
        self.window.destroy()

    def go_not_perfect_page(self):
        self.window.destroy()

    def go_best_class_page(self):
        self.window.destroy()