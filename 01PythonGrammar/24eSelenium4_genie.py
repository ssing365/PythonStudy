import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = 'https://www.genie.co.kr/chart/top200'
driver.get(url) 

# 얻어온 HTML소스를 파싱하기 위해 Soup객체로 변환
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 파싱한 정보를 저장하기 위해 리스트 생성
song_data = []
rank = 1
# 1~4페이지까지 순차적으로 반복
for page in range(1,5):
    print("페이지", page)
    # 묵시적 대기 2초
    driver.implicitly_wait(2)   
    # 차트가 있는 테이블에서 반복되는 <tr>요소를 얻어옴
    songs = soup.select('tbody>tr')
    
    for song in songs:
        title = song.select('a.title')[0].text.strip()
        singer = song.select('a.artist')[0].text
        # 제목, 가수, 순위까지 새로운 리스트를 생성후 추가
        song_data.append(['Genie', rank, title, singer])
        rank += 1
    # 페이지 바로가기 버튼의 XPath를 파악 후 f-String으로 처리
    if page < 4 :
        driver.find_element(
            By.XPATH,
            f'//*[@id="body-content"]/div[7]/a[{page+1}]'
        ).click()
    driver.implicitly_wait(5)   
    #1~4페이지까지 페이지번호 링크를 누르며 순차적으로 크롤링
    
#크롤링이 완료되면 판다스를 이용해 엑셀로 저장
columns = ['서비스', '순위', '타이틀', '가수']
pd_data = pd.DataFrame(song_data, columns=columns)
print(pd_data.head()) #데이터 확인
pd_data.to_excel('./saveFiles/genie_chart.xlsx', index=False)