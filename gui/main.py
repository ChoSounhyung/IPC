from tkinter import *
from gui.student_menu import *

start_page_window = Tk()

def main():
    start_page_window.title("IPC")
    start_page_window.config(bg='#272727')
    start_page_window.geometry("1000x650+250+70")
    start_page_window.resizable(False, False)
    StartPage(start_page_window)
    start_page_window.mainloop()

def student_page(event):
    print("Student")
    student_page_window = Tk()
    student_page_window.title("IPC")
    student_page_window.config(bg='#272727')
    student_page_window.geometry("1000x650+250+70")
    student_page_window.resizable(False, False)
    StudentPage(student_page_window)
    student_page_window.mainloop()

def teacher_page(event):
    print("Teacher")
    teacher_page_window = Tk()
    teacher_page_window.title("IPC")
    teacher_page_window.config(bg='#272727')
    teacher_page_window.geometry("1000x650+250+70")
    teacher_page_window.resizable(False, False)
    #TeacherPage(teacher_page_window)
    start_page_window.destroy()
    teacher_page_window.mainloop()

class StartPage(Frame):
    def __init__(self, master):
        title = Label(text="IPC", bg='#272727', fg='#51F591', font=("Arial 60 bold"))
        explain = Label(text=": 앱설명앱설명앱설명앱설명앱설명앱설명앱설명앱설명", bg='#272727', fg='#51F591',
                        font=("System 13 normal"))

        student_btn = PhotoImage(file='../image/student_btn.png')
        student_label = Label(image=student_btn, bg='#272727')
        student_label.image = student_btn
        student_label.bind("<Button-1>", student_page)

        teacher_btn = PhotoImage(file='../image/teacher_btn.png')
        teacher_label = Label(image=teacher_btn, bg='#272727')
        teacher_label.image = teacher_btn
        teacher_label.bind("<Button-1>", teacher_page)

        title.place(x=140, y=180, anchor='nw')
        explain.place(x=140, y=270, anchor='nw')
        student_label.place(x=140, y=360)
        teacher_label.place(x=320, y=360)


if __name__ == '__main__':
    main()