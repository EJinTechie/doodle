i_list=list(input("정수 입력 : ").split())

def to_float(x):
    return float(x)

F1_list=list(map(to_float,i_list))
F2_list=list(map(lambda x:float(x),i_list))
# F3_list=[float(x) for x in i_list]
F3_list=[to_float(x) for x in i_list]
F4_list=list(map(to_float,i_list))

print(f"i_list = {i_list}")
print(f"F1_list = {F1_list}")
print(f"F2_list = {F2_list}")
print(f"F3_list = {F3_list}")
print(f"F4_list = {F4_list}")
