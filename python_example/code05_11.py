outFp = None
outStr = ""

outFp = open("C:/Users/user/Desktop/hangeul.txt","w")


while True : 
    outStr = input("내용 입력 : ")
    if outStr != "" :
        outFp.writelines(outStr + "\n")
    else :
        break

outFp.close()
print("--정상적으로 파일에 입력되셨습니다! ^,^")        