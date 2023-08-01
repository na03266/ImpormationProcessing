from tkinter import *

window = Tk()

label1=Label(window, text="COOKBOOK, 데이터분석을") #뒤에 폰트나 정보가 없어서 디폴트 값으로 적힘
label2=Label(window, text="열심히", font=("궁서체",30),fg = "blue") #폰트, 글씨 크기를 설정하여, 조건대로 바꿔서 적힘 
label3=Label(window, text="공부 하기 싫다!!!!!!!!!!!!!!!!!.", bg = "magenta", width = 20,height = 5, anch or = SE)
#bg = background, 배경색 바꾸기다! 옆에 width, height는 배경 크기 이야기 하는 거 ㅇㅇ

label1.pack() #
label2.pack()
label3.pack()

window.mainloop()

#오류가 많던데 나중에 고쳐둘것