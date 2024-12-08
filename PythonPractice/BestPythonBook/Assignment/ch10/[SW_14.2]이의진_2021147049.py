num = [1,2,3,4,5,6,7,8,9,10]
def is_even(i):
    if i%2==0:
        return True
    else:
        return False

E1_list=[]
for i in num:
    if is_even(i):
        E1_list.append(i)

print(f"E1_list = {E1_list}")