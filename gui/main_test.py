from tkinter import *
from start_page import StartPage
from student_page import StudentPage

def main():
    StartPage()


def click_handler(event):
    student_window = Tk()
    student_window.title("IPC")
    student_window.geometry("1000x650+250+70")
    student_window.config(bg='#272727')
    student_window.resizable(False, False)
    StudentPage(student_window)
    student_window.mainloop()


if __name__ == '__main__':
  main()