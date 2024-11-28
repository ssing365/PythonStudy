import time
from datetime import date, datetime, timedelta

today = date.today()
print('오늘날짜', today, today.year, today.month, today.day)    

print("="*30)

dtime = datetime.now()
print('현재시각', dtime)
print('년/월/일', dtime.year, dtime.month, dtime.day)
print('시/분/초/밀리세컨즈', dtime.hour, dtime.minute, dtime.second, dtime.microsecond)

print("="*30)

#날짜 계산1
one_day = timedelta(days=1)
yesterday = today - one_day
tomorrow = today + one_day
print("어제와 오늘", yesterday, tomorrow)

#날짜 계산2
date_diff = today - yesterday
print("날짜 차이", date_diff)

#날짜 형식
date_str = today.strftime("%Y-%m-%d")
print("형식 지정",date_str)

#크리스마스까지 남은 날짜 계산
x_mas_str = f'{today.year}-12-25'  
x_mas_datetime = datetime.strptime(x_mas_str, '%Y-%m-%d')
x_mas_date = datetime.date(x_mas_datetime)
print(x_mas_str, x_mas_datetime, x_mas_date)
print(type(x_mas_str), type(x_mas_datetime), type(x_mas_date))
date_diff = x_mas_date-today
print("크리스마스까지1", date_diff)
print("크리스마스까지2", date_diff.days)