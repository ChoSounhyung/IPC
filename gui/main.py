from tkinter import *

window = Tk()

window.title("IPC")
window.config(bg='#272727')
window.geometry("1000x650+100+100")
window.resizable(False, False)

title = Label(window, text="IPC", bg='#272727', fg='#51F591', font=("Arial 60 bold"))
explain = Label(window, text=": 앱설명앱설명앱설명앱설명앱설명앱설명앱설명앱설명", bg='#272727', fg='#51F591', font=("System 13 normal italic"))


student_btn = PhotoImage(file='../image/student_btn.png')
student_label = Label(image=student_btn, bg='#272727')

teacher_btn = PhotoImage(file='../image/teacher_btn.png')
teacher_label = Label(image=teacher_btn, bg='#272727')

title.place(x=140, y=180, anchor='nw')
explain.place(x=140, y=270, anchor='nw')
student_label.place(x=140, y=360)
teacher_label.place(x=320, y=360)

window.mainloop()