import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = 'https://music.bugs.co.kr/chart'
driver.get(url) 

# 얻어온 HTML소스를 파싱하기 위해 Soup객체로 변환
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 파싱한 정보를 저장하기 위해 리스트 생성
song_data = []
rank = 1

driver.implicitly_wait(5) 

songs = soup.select('#CHARTrealtime > table > tbody > tr')
print(songs)
for song in songs:
    title = song.select_one('th > p > a').get_text()
    singer = song.select_one('td:nth-child(8) > p > a').get_text()
    album = song.select_one('td:nth-child(9) > a').get_text()
    #CHARTrealtime > table > tbody > tr:nth-child(1) > th > p > a 제목
    #CHARTrealtime > table > tbody > tr:nth-child(1) > td:nth-child(8) > p > a 가수
    #CHARTrealtime > table > tbody > tr:nth-child(1) > td:nth-child(9) > a 앨범
    song_data.append(['Bugs!', rank, title, singer, album])
    rank += 1
    print("*"*40)
driver.implicitly_wait(5)

columns = ['서비스', '순위', '타이틀', '가수', '앨범']
pd_data = pd.DataFrame(song_data, columns=columns)
print(pd_data.head()) #데이터 확인
pd_data.to_excel('./saveFiles/bugs_chart.xlsx', index=False)