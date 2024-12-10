f=open("data5.txt",'w')
for i in range(5):
    n=input("다섯가지 정수를 입력하시오 : ")
    f.write(n)
    f.write('\n')
f.close()