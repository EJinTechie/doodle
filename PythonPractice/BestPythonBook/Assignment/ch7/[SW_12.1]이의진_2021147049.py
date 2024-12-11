import random as rd
cnt={}
for i in range(10000):
    a = rd.randrange(1, 7)
    if a in cnt:
        cnt[a]+=1
    else:
        cnt[a]=1

for k in range(1,7):
    print(f"{k} {cnt[k]}  {cnt[k]/10000}")
