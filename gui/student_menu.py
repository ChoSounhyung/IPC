from tkinter import *

def search_ip_page(event):
    print("Search IP")

class StudentPage:
    def __init__(self, master):
        search_ip_btn = PhotoImage(master=master, file='../image/search_ip_btn.png')
        search_ip_label = Label(master, image=search_ip_btn, bg="#272727")
        title = Label(master, text="IPC", bg='#272727', fg='#51F591', font=("Arial 60 bold"))
        title.place(x=140, y=180, anchor='nw')

        search_ip_label.place(x=200, y=200)
        search_ip_label.bind("<Button-1>", search_ip_page)
