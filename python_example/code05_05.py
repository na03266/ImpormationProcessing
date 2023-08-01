from tkinter import *
from tkinter import messagebox

#함수 선언
def myFunc() : 
    messagebox.showinfo("강아지 버튼", "강아지  졸귀탱")

window = Tk()

photo = PhotoImage(file="C:/Users/user/Desktop/source (2)/GIF/dog8.gif")
# 파일 속성에 들어가서 경로 붙여넣기 하고 슬래시 / 이걸로 바꾼담에 파일명 까지 꼭!!!!! 붙여넣기  
button1 = Button(window, image=photo, command=myFunc)

button1.pack()

window.mainloop()