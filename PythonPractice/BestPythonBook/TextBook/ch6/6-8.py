s=(1,2,5,4,3,2,9,1,4,7,8,9,9)
duplicate=[]
for num in set(s):
    if s.count(num)>1:
        duplicate.append(num)
print(f"중복 원소는 {set(duplicate)}")
