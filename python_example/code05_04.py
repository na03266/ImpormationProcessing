from tkinter import *
window = Tk()
#Tk가 머임?

button1 = Button(window, text="파이썬 종료", fg="red",command= quit) 
#command = 명령, text = 버튼에 들어갈 텍스트, window = 창 열기


button1.pack()

window.mainloop()

