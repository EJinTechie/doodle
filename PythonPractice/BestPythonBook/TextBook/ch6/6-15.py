given=(4,5,2,3,8,1,9,0)
g_l=list(given)
for i in range(0,len(g_l)):
    while len(g_l)>1:
        g_l.pop()
        print(tuple(g_l))