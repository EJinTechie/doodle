n_list=[-22.3,29.44,902.2,45.7,-887.1,-56.3]
print(f"최댓값 : {max(n_list)}")
print(f"최솟값 : {min(n_list)}")

def my_max(x):
    max_v=x[0]
    for num in x:
        if num > max_v:
            max_v=num
    return max_v

def my_min(x):
    min_v=x[0]
    for num in x:
        if num < min_v:
            min_v=num
    return min_v

print(f"최댓값 : {my_max(n_list)}")
print(f"최솟값 : {my_min(n_list)}")

from functools import reduce
max_value=reduce(lambda x,y :x if x>y else y,n_list)
min_value=reduce(lambda x,y :x if x<y else y,n_list)
print(f"최댓값 : {max_value}")
print(f"최솟값 : {min_value}")