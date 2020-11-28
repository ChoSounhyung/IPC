from tkinter import *

class StudentPage:
    def __init__(self):
        self.window = Tk()
        self.window.title("IPC")
        self.window.geometry("1000x650+250+70")
        self.window.config(bg='#272727')
        self.window.resizable(False, False)

        search_ip_image = PhotoImage(file='../image/search_ip_btn.png')
        search_ip_click = Button(borderwidth=0, command=self.go_search_ip_page, bg='#272727', activebackground='#272727')
        search_ip_click.place(x=140, y=180, anchor='nw')
        search_ip_click.config(image=search_ip_image)

        mypc_image = PhotoImage(file='../image/mypc_prot_btn.png')
        mypc_click = Button(borderwidth=0, command=self.go_search_ip_page, bg='#272727', activebackground='#272727')
        mypc_click.place(x=540, y=180, anchor='nw')
        mypc_click.config(image=mypc_image)

        self.window.mainloop()

    def go_search_ip_page(self):
        self.window.destroy()

    def go_mypc_page(self):
        self.window.destroy()