'''
퀴즈] 
https://www.daum.net/ 접속 후 카카오계정으로 로그인 버튼 클릭
==> 아이디,비번 입력 후 로그인 버튼 클릭 ==> 메인으로 이동
==> 검색어 입력 후 검색결과 페이지 확인 
''' 

#셀레니움 모듈과 드라이버 로드
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#드라이버 로드
driver = webdriver.Chrome()

#네이버 메인 접속
url = 'https://www.daum.net/'  
driver.get(url)

#XPath를 이용해서 네이버 메인의 로그인 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="loginMy"]/div/div[1]/div/a').click()
#로드와 상관없이 무조건 2초 대기
time.sleep(2)

#로그인페이지로 이동 후 아이디/비번의 입력상자를 찾은 후 본인의 정보 입력
driver.find_element(By.NAME, 'loginId').send_keys('ssing365@naver.com')   
time.sleep(2)
driver.find_element(By.NAME, 'password').send_keys('lhsung1130')
time.sleep(2)

#입력 후 로그인 버튼을 클릭해서 로그인 시도
driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[1]/form/div[4]/button[1]').click()
#셀레니움 로그인을 감지하므로 캡챠(자동로그인 방지)화면이 뜬다.
time.sleep(25)
#조금 긴 시간을 대기하면서 직접 입력한다.

driver.find_element(By.XPATH, '//*[@id="q"]').click()
time.sleep(2)

#로그인이 완료되면 메인으로 자동 이동하므로 상단의 검색창에 검색어를 입력
driver.find_element(By.NAME, 'q').send_keys('결혼해유 시청률')
time.sleep(2)

#검색 버튼을 눌러 결과 확인
driver.find_element(By.CLASS_NAME, 'btn_ksearch').click()
time.sleep(10)