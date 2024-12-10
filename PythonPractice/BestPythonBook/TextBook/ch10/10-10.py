lst=[]
for i in range(1,100):
    if i%6==0 and i%7==0:
        lst.append(i)
print(lst)

new_list0=list(filter(lambda x:x%6==0 and x%7==0,range(1,100)))
print(new_list0)

new_list=[x for x in range(1,100) if x%6==0 and x%7==0]
print(new_list)