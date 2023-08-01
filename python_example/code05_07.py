from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def func_open() :
    messagebox.showinfo("메뉴선택", "열기 메뉴를 선택함")

def func_exit() :
    window.quit()
    window.destroy()

## 메인 코드 부분 ##
window = Tk()

mainMenu = Menu(window)
