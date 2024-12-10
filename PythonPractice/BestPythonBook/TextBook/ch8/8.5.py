f=open('numbers.txt','w')
f.write("100\n200\n300\n400")
f.close()

f=open('numbers.txt','r')
for i in range(4):
    s=f.readline().rstrip()
    print(s)
f.close()