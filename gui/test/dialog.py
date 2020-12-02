from tkinter import *
import tkinter.messagebox

def Info():
    tkinter.messagebox.showinfo("info", "정보 알려주는 용도\n(파란 느낌표)")

def Warning():
    tkinter.messagebox.showwarning("warning", "경고 알려주는 용도\n(노란 느낌표)")

def Error():
    tkinter.messagebox.showerror("error", "경고 알려주는 용도\n(빨간 엑스)")

def AskQuestion():
    tkinter.messagebox.askquestion("question", "질문할때\n(파란 물음표)")

def OkCancel():
    tkinter.messagebox.askokcancel("ok or cancel", "확인 or 취소\n(파란 물음표)")

def YesNo():
    tkinter.messagebox.askyesno("yes or no", "확인 or 취소\n(파란 물음표)")

def AskRetryCancel():
    tkinter.messagebox.askretrycancel("retry or cancel", "다시 시도 or 취소\n(노란 느낌표)")

def close_win():
    win.destroy()
    win.quit()

win = Tk()
win.title("메세지 상자")

base_frm = Frame(win)
base_frm.pack()

btn_info = Button(base_frm, text="info", width="40", command = Info)
btn_info.pack(pady="10")
btn_warning = Button(base_frm, text="warning", width="40", command = Warning)
btn_warning.pack(pady="10")
btn_error = Button(base_frm, text="error", width="40", command = Error)
btn_error.pack(pady="10")
btn_question = Button(base_frm, text="question", width="40", command = AskQuestion)
btn_question.pack(pady="10")
btn_ok_cancel = Button(base_frm, text="ok or cancel", width="40", command = OkCancel)
btn_ok_cancel.pack(pady="10")
btn_yes_no = Button(base_frm, text="yes or no", width="40", command = YesNo)
btn_yes_no.pack(pady="10")
btn_retry_cancel = Button(base_frm, text="retry or cancel", width="40", command = AskRetryCancel)
btn_retry_cancel.pack(pady="10")

win.mainloop()