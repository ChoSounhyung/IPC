import tkinter

window = tkinter.Tk()

window.title("IPC")
window.config(bg='#272727')
window.geometry("700x450+100+100")
window.resizable(False, False)


label = tkinter.Label(window, text="IPC", bg='#272727', fg='#51F591', font=("Arial 40 bold"))
label.place(x=80, y=90, anchor='nw')

window.mainloop()