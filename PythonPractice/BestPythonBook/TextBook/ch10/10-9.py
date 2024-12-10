lst=[]
for i in range(0,100):
    if i%6==0:
        lst.append(i)
print(lst)

new_list0=list(filter(lambda x:x%6==0,range(0,100)))
print(new_list0)

new_list=[x for x in range(0,100,6)]
print(new_list)