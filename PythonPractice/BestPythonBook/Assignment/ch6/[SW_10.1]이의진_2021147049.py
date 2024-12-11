name = ['카페아메리카노','돌체라떼','카페모카','화이트초코모카']
code = ['CA', 'DL', 'CM', 'WM']
price = [4500, 5900, 5500, 5900]
cnt = [0, 0, 0, 0]
total=[0, 0, 0, 0]
order = 'hi'
while order != 'Q':
    order = input('주문 코드 입력 : ')
    if order == 'CA':
        print(f"주문하신 음료는 {name[0]} 이고, 가격은 {price[0]}")
        cnt[0]+=1
        total[0]+=1
    if order == 'DL':
        print(f"주문하신 음료는 {name[1]} 이고, 가격은 {price[1]}")
        cnt[1]+=1
        total[1]+=1
    if order == 'CM':
        print(f"주문하신 음료는 {name[2]} 이고, 가격은 {price[2]}")
        cnt[2]+=1
        total[2]+=1
    if order == 'WM':
        print(f"주문하신 음료는 {name[3]} 이고, 가격은 {price[3]}")
        cnt[3]+=1
        total[3]+=1

print(f"{name[0]}  {cnt[0]}  {4500*total[0]}")
print(f"{name[1]}  {cnt[1]}  {5900*total[1]}")
print(f"{name[2]}  {cnt[2]}  {5500*total[2]}")
print(f"{name[3]}  {cnt[3]}  {5900*total[3]}")
