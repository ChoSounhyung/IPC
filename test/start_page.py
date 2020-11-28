from tkinter import *
from student_page import StudentPage

class StartPage:
  def __init__(self):
    self.window = Tk()
    self.window.title("Start")
    self.window.geometry("300x300")

    img_click = PhotoImage(file="next.png")
    btn_click = Button(width=150, height=150, borderwidth=0, command=self.go_student_page)
    btn_click.place(x=0, y=0)
    btn_click.config(image=img_click)

    self.window.mainloop()

  def go_student_page(self):
    self.window.destroy()
    StudentPage()
