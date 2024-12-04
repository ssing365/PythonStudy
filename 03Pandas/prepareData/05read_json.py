# -*- coding: utf-8 -*-
import pandas as pd
#웹페이지의 정보를 얻어오기 위해 필요한 모듈
import requests

#JSON 파일을 데이터프레임으로 변환
df1 = pd.read_json('../resData/sample.json')
print(df1)

print("="*30)   

# 인덱스만 출력
print(df1.index)
# 라벨형 인덱스를 통해 요소에 접근
print("마지막 데이터 : ", df1.loc['Paul','c++'])
#컬럼 전체를 출력할 때는 데이터프레임명만 사용
print("첫 번째 컬럼")
print(df1['algol'])

#행 전체를 출력할 때는 loc(혹은 iloc)을 사용
print("첫번째 행 : ")
print(df1.loc['Jerry'])

print("="*30)   

#외부 JSON 
url = 'https://koreanjson.com/users'
#웹 url을 지정해 정보를 얻어온다.
response = requests.get(url)

if response.status_code == 200:
    #JSON 데이터를 얻어온 후 데이터프레임으로 변환
    jsonData = response.text
    df2 = pd.read_json(jsonData)    
    #id컬럼을 인덱스로 지정 후 원본에 적용
    df2.set_index('id', inplace=True)
    print(df2)
else:
    print("API 연동 중 오류 발생")
    print(response.status_code)