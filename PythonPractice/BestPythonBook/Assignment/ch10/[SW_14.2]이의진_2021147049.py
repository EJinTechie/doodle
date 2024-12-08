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

E2_list=[]
for b in filter(lambda n: n%2==0,num):
    E2_list.append(b)

#[표현식 for 변수 in 반복자/연속열]
E3_list=[x for x in num if x%2==0]

E4_list=list(filter(lambda n:n%2==0,num))


print(f"E1_list = {E1_list}")
print(f"E2_list={E2_list}")
print(f"E3_list={E3_list}")
print(f"E4_list={E4_list}")