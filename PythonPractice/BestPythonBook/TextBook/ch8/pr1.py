f=open("numbers.txt",'r')
i=0
for i in range(4):
    s=f.readline().rstrip()
    print(s)
f.close()