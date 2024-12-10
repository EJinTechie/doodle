n_list=[-22.3,29.44,902.2,45.7,-887.1,-56.3]
print(f"최댓값 : {max(n_list)}")
print(f"최솟값 : {min(n_list)}")

def my_min(numbers):
    min_value=numbers[0]
    for num in numbers:
        if num<min_value:
            min_value = num
    return min_value

def my_max(numbers):
    max_value =numbers[0]
    for num in numbers:
        if num>max_value:
            max_value=num
    return max_value

print(my_max(n_list))
print(my_min(n_list))