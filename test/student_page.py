from tkinter import *


class StudentPage:
  def __init__(self):
    self.window = Tk()
    self.window.title("Student")
    self.window.geometry("400x400")

    img_good = PhotoImage(master=self.window, file="good.png")
    lbl_good = Label(master=self.window, image=img_good)
    lbl_good.place(x=100, y=100)

    self.window.mainloop()
