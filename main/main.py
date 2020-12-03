from tkinter import *
from gui.start_page import StartPage

def main():
    StartPage()


def click_handler(event):
    new_window = Tk()
    new_window.title("IPC")
    new_window.geometry("1000x650+250+70")
    new_window.config(bg='#272727')
    new_window.resizable(False, False)
    new_window.mainloop()

if __name__ == '__main__':
  main()