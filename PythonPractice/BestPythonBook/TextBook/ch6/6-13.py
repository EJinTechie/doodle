given=[5,6,3,9,2,12,3,8,7]
for k in range(len(given),0,-1):
    for i in range(0,k):
        if given[i]==max(given[:k]):
            given[i],given[k-1]=given[k-1],given[i]
print(given)