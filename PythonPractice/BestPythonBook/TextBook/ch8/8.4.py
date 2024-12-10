f=open('foo.txt','r')
for i in range(3):
    s=f.readline()
    print(s,end='')
f.close()

f=open('foo.txt','r')
s=f.readline().rstrip()
print(s)
s=f.readline().rstrip()
print(s)
s=f.readline().rstrip()
print(s)
f.close()