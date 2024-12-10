n_list=[-22.3,29.44,902.2,45.7,-887.1,-56.3]
new_list=[]
for i in n_list:
    if i>0:
        new_list.append(i)
print(new_list)

new_list1=list(filter(lambda x:x>0,n_list))
print(new_list1)

new_list2=[x for x in n_list if x>0]
print(new_list2)