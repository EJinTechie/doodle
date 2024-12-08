a_list=list(input("소문자 입력 : "))

def to_upper(x):
    return x.upper()

A1_list=list(map(to_upper,a_list))

A2_list=[]
for i in range(0,len(a_list)):
    A2_list.append((lambda i:a_list[i].upper())(i))

# A3_list=[x for x in map(to_upper,a_list)]
A3_list=[x.upper() for x in a_list]

A4_list=[]
for _ in a_list:
    A4_list=list(map(lambda x:x.upper(),a_list))

print(f"a_list = {a_list}")
print(f"A1_list = {A1_list}")
print(f"A2_list = {A2_list}")
print(f"A3_list = {A3_list}")
print(f"A4_list = {A4_list}")