lyrics = 'Half of my heart is in Havana'
a=list(lyrics.split())
b=list(map(lambda x:x.upper(),a))
abc=[]
for i in range(len(b)):
    ab = []
    ab.append(a[i])
    ab.append(b[i])
    k=tuple(ab)
    abc.append(k)
print(abc)