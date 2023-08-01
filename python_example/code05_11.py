outFp = None
outStr = ""

outFp = open("C:/Users/user/Desktop/hangeul.txt","w")
# 파일 절대주소로 잡아두고, 해당 파일에 입력할 것 선언? 


while True : 
    outStr = input("내용 입력 : ") #내용 입력 칸 만들기
    if outStr != "" : #공백을 입력하지 않는다면 계속 진행
        outFp.writelines(outStr + "\n")
    else : #그게 아닐시 break(탈출)문을 통하여 끝내기.
        break

outFp.close() #닫기
print("--정상적으로 파일에 입력되셨습니다! ^,^")     #해당 구문 출력