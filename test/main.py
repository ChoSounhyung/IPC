from tkinter import *
from start_page import StartPage
from student_page import StudentPage


def main():
  StartPage()


def click_handler(event):
  window2 = Tk()
  window2.geometry("400x400")
  StudentPage(window2)
  window2.mainloop()


if __name__ == '__main__':
  main()
