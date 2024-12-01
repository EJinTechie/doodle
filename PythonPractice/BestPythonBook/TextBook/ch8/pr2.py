f=open("data5.txt",'r')
su=0
for _ in range(5):
    n=int(f.readline())
    su+=n
print(su/5)
f.close()