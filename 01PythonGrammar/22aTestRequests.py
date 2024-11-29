import requests
url = 'https://ikosmo.co.kr/main'
response1 = requests.get(url, headers={"User-Agent" : "Mozilla/5.0"} )
#print(response1.status_code) # 응답코드를 출력
#print(response1.text) # HTML 코드를 출력

#네이버 블로그 검색 세션에서 사용할 수 있는 쿼리스트링은 json형태로 작성한다.
paramJson = {
    'pageNo' : 1,
    'rangeType' : 'ALL',
    'orderBy' : 'sim',
    'keyword' : '파이썬 웹크롤링'
}
response2 = requests.get('https://section.blog.naver.com/Search/Post.nhn', params=paramJson)
#print(response2.status_code) # 응답코드를 출력
#print(response2.text) # HTML 코드를 출력

from bs4 import BeautifulSoup

url = 'http://daum.net/'
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
else : 
    print(response.status_code)