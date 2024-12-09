given1=[5,6,31,9,2,12,13,8,7]
given=[5,6,31,9,2,12,13,8,7]
n=1
lst1=[]
print(f"정렬전 리스트 : {given1}")
for k in range(len(given),0,-1):
    for i in range(0,k):
        if given[i]==max(given[:k]):
            lst1.append(given[i])
            given.remove(given[i])
            if n!=9:
                print(f"{n} 단계 : {given},{lst1}")
                n+=1
            else:
                print(f"정렬된 리스트 : {lst1}")
            break
