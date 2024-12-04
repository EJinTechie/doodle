list=[-30,45,-5,-90,20,53,77,-36]
def minus_func(n):
    if n<0:
        return True
    else:
        return False

lst = []
for n in list:
    if minus_func(n):
        lst.append(n)

print(lst)


