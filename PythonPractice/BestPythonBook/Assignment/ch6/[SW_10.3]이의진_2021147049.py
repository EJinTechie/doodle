name = {'CA':'카페아메리카노','DL':'돌체라떼','CM':'카페모카','WM':'화이트초코모카'}
price = {'CA':4500,'DL':5900,'CM':5500,'WM':5900}
cnt = {'CA':0,'DL':0,'CM':0,'WM':0}
total= {'CA':0,'DL':0,'CM':0,'WM':0}

order='hi'
while order != 'Q':
    order=input('주문 코드 입력 : ')
    if order in name:
        print(f"주문하신 음료는 {name[order]} 이고 , 가격은 {price[order]}")
        cnt[order]+=1
        total[order]+=4500

for k in name:
    print(f"{name[k]}   {cnt[k]}  {total[k]}")