fruit_dic = {'apple': 4, 'mango': 10, 'banana': 3, 'kiwi': 4}
fruit=input('확인할 과일 이름 : ')
if fruit in fruit_dic:
    print(f"{fruit}는(은) 냉장고 속에 있음")
print("냉장고 속 과일의 종류와 개수")
for k in fruit_dic:
    print(f"{k} : {fruit_dic[k]}개")