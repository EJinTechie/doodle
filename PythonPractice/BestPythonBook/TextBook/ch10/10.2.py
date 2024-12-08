# def minus_func(n):
#     if n<0:
#         return True
#     else:
#         return False

n_list=[-30,-29,15,34,-34,-76]
#n_list1=[]
#for n in n_list:
#    if minus_func(n):
#        n_list1.append(n)
#print(n_list1)

minus_list=[]
n_function=lambda n : n<0
for n in filter(n_function,n_list):
    minus_list.append(n)
print(minus_list)
# n_function=lambda n: n<0
# n_list1=list(filter(n_function,n_list))
# print(n_list1)