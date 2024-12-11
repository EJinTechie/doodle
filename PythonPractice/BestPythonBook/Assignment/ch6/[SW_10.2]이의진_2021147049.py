name = {'CA':'카페아메리카노','DL':'돌체라떼','CM':'카페모카','WM':'화이트초코모카'}
price = {'CA':4500,'DL':5900,'CM':5500,'WM':5900}
cnt = {'CA':0,'DL':0,'CM':0,'WM':0}
total= {'CA':0,'DL':0,'CM':0,'WM':0}

order='hi'
while order != 'Q':
    order=input('주문 코드 입력 : ')
    if order in name.keys():
        if order == 'CA':
            print(f"주문하신 음료는 {name['CA']} 이고 , 가격은 {price['CA']}")
            cnt['CA']+=1
            total['CA']+=4500
        if order == 'DL':
            print(f"주문하신 음료는 {name['DL']} 이고 , 가격은 {price['DL']}")
            cnt['DL'] += 1
            total['DL'] += 5900
        if order == 'CM':
            print(f"주문하신 음료는 {name['CM']} 이고 , 가격은 {price['CM']}")
            cnt['CM']+=1
            total['CM']+=5500
        if order == 'WM':
            print(f"주문하신 음료는 {name['WM']} 이고 , 가격은 {price['WM']}")
            cnt['WM']+=1
            total['WM']+=5900
print(f"{name['CA']}   {cnt['CA']}  {total['CA']}")
print(f"{name['DL']}   {cnt['DL']}  {total['DL']}")
print(f"{name['CM']}   {cnt['CM']}  {total['CM']}")
print(f"{name['WM']}   {cnt['WM']}  {total['WM']}")
