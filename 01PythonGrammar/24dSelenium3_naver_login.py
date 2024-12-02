#셀레니움 모듈과 드라이버 로드
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#드라이버 로드
driver = webdriver.Chrome()

#네이버 메인 접속
url = 'https://www.naver.com/'  
driver.get(url)

#XPath를 이용해서 네이버 메인의 로그인 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="account"]/div/a').click()
#로드와 상관없이 무조건 2초 대기
time.sleep(2)

#로그인페이지로 이동 후 아이디/비번의 입력상자를 찾은 후 본인의 정보 입력
driver.find_element(By.NAME, 'id').send_keys('ssing365')   
time.sleep(2)
driver.find_element(By.NAME, 'pw').send_keys('hossingssing')
time.sleep(2)

#입력 후 로그인 버튼을 클릭해서 로그인 시도
driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
#셀레니움 로그인을 감지하므로 캡챠(자동로그인 방지)화면이 뜬다.
time.sleep(30)
#조금 긴 시간을 대기하면서 직접 입력한다.

#로그인이 완료되면 메인으로 자동 이동하므로 상단의 검색창에 검색어를 입력
driver.find_element(By.NAME, 'query').send_keys('결혼해유 시청률')
time.sleep(2)

#검색 버튼을 눌러 결과 확인
driver.find_element(By.CLASS_NAME, 'btn_search').click()
time.sleep(10)