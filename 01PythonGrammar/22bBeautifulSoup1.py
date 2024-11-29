'''
웹크롤링을 위해 필요한 모듈(패키지)
requests : 웹페이지의 소스(HTML)을 가져온다.
BeautifulSoup : 얻어온 HTML에서 필요한 정보를 추출(Parsing)한다.
'''
import requests
from bs4 import BeautifulSoup

#크롤링 할 웹사이트 URL
url = 'https://kin.naver.com/search/list.naver?query=%EC%9B%B9%ED%81%AC%EB%A1%A4%EB%A7%81'
#requests를 통해 HTML소스를 얻어옴
response = requests.get(url)

#응답코드가 200이면 정상 접속된 상태로 판단
if response.status_code == 200:
    #HTML코드를 변수에 저장
    html = response.text
    #파싱을 위해 soup 객체로 변환. HTML코드이므로 html파서를 적용
    soup = BeautifulSoup(html, 'html.parser')
    
    #셀렉터로 추출(크롬 개발자도구에서 copy selector) : 검색결과에서 첫번째 제목을 파싱
    title1_1 = soup.select_one('#s_content > div.section > ul > li:nth-child(1) > dl > dt > a')
    print("추출1_1 : ", title1_1)
    
    #HTML태그는 모두 제거하고 텍스트만 파싱
    text = title1_1.get_text()
    #print("추출2 : ", text)
    
    '''
    검색결과 10개를 표현한 <ul>태그 하위의 <li>를 한꺼번에 가져오기 위해 아래와 같이 파싱한다.
    '''
    ul = soup.select_one('ul.basic1')
    #10개의 <li>태그 전체가 출력된다.
    #print("추출3 : ", ul)
    
    print(f"{'추출4':-^30}")
    #추출3에서 가져온 <ul>태그에서 반복되는 <li>를 얻어온다.
    titles2 = ul.select('li > dl > dt > a')
    #그리고 개수만큼 반복해서 파싱한다.
    for tit in titles2:
        #즉 검색결과 페이지에서 제목만 파싱하여 출력한다.
        print(tit.get_text())
else:
    print(response.status_code)
    
#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody