import requests
from bs4 import BeautifulSoup

url = "https://www.lotto.co.kr/"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

div = soup.select_one('div.current_result')
#print(div)

# 회차 추출
draw_no_strong = div.select_one('strong')
draw_no = draw_no_strong.get_text()

# 추첨 날짜 추출
draw_date_i = div.select_one('i')
draw_date = draw_date_i.get_text().replace("추첨", "")

# 당첨 번호 추출
lotto_numbers = []
bonus_num = '0'
lotto_balls = div.select('img')
for lotto_ball in lotto_balls:
    ball_str = str(lotto_ball)
    if '/on/' in ball_str:
        ball_num = ball_str.split("/on/")[-1].split(".")[0]
        lotto_numbers.append(ball_num)
    elif '/bonus/' in ball_str:
        bonus_num_str = ball_str.split("/bonus/")[-1].split(".")[0]
        bonus_num = bonus_num_str

# 결과 출력
print('추첨 회차 : ', draw_no)
print('추첨 날짜 : ', draw_date)
print('당첨 번호 : ', lotto_numbers)
print('보너스 번호 : ', bonus_num)