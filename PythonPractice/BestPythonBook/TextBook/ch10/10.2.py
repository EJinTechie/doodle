adult_func=lambda n: n>=19
ages =[34,32,29,18,13,54]
for a in filter(adult_func,ages):
    print(a,end=' ')

    #filter(적용할 함수, 적용할 대상)