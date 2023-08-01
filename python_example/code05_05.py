from tkinter import *
from tkinter import messagebox

#함수 선언
def myFunc() : 
    messagebox.showinfo("강아지 버튼", "강아지  졸귀탱")

window = Tk()

photo = PhotoImage(file="C:/Users/user/Desktop/source (2)/GIF/dog8.gif")
button1 = Button(window, image=photo, command=myFunc)

button1.pack()

window.mainloop()