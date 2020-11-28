from tkinter import *
from start_page import StartPage
from student_page import StudentPage
from teacher_page import TeacherPage

def main():
    StartPage()


def click_handler(event):
    new_window = Tk()
    new_window.title("IPC")
    new_window.geometry("1000x650+250+70")
    new_window.config(bg='#272727')
    new_window.resizable(False, False)
    StudentPage(new_window)
    TeacherPage(new_window)
    new_window.mainloop()


if __name__ == '__main__':
  main()