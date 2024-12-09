import datetime as dt
start_day= dt.date.today().replace(year=2019, month=2, day=24)
today= dt.date.today()
print(f"춘향이와 몽룡이의 연애 시작일 : {start_day}")
num= today-start_day
print(f"연애 시작일로부터 경과한 날짜 : {num.days}일")
hundred=dt.timedelta(100)
twohundred=dt.timedelta(200)
fivehundred=dt.timedelta(500)
thousand=dt.timedelta(1000)
print(f"100일 기념일 : {today+hundred}")
print(f"200일 기념일 : {today+twohundred}")
print(f"500일 기념일 : {today+fivehundred}")
print(f"1000일 기념일 : {today+thousand}")

