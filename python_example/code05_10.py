inFp = None
inStr = "" 

inFp = open("C:/Users/user/Desktop/hangeul.txt", "r")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end= "")

inFp.close()
