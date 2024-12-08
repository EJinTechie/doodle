from functools import reduce
a,b,n=map(int,input(" a b n 입력 : ").split())
lst=[]
for i in range(a,b+1):
    lst.append(i)
lst1=[]
for _ in range(1,n+1):
    lst1.append(_)
sum1=reduce(lambda x,y:x+y,lst)
mult=reduce(lambda x,y:x*y,lst1)
print(f"{a}에서 {b}까지의 합 : {sum1}")
print(f"{n}! = {mult}")