import random as rd
menu=['돈까스', '라멘', '파스타', '제육볶음', '김치찌게', '자장면','칼국수']
a=int(input("메뉴 개수 입력 : "))
print(rd.choices(menu,k=a))