a=input("type the file name : ")
f=open(a,'r')
n=1
l=f.readline()
while l:
    print(f"{n} {l}",end='')
    n+=1
    l=f.readline()
f.close()
