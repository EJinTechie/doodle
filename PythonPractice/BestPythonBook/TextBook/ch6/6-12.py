given=[5,6,3,9,2,12,3,8,7]
print(max(given))
print(len(given))
for i in range(0,len(given)):
    if given[i]==max(given):
        given[i],given[len(given)-1]=given[len(given)-1],given[i]
print(given)