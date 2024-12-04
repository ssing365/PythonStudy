# -*- coding: utf-8 -*-
import pandas as pd
#웹페이지의 table을 가져오기 위해서는 lxml모듈이 설치되어 있어야한다.

url = '../resData/sample.html' 
tables = pd.read_html(url)

#샘플 파일에는 테이블이 2개 존재한다.
print('테이블 개수 : ', len(tables))

#테이블의 개수만큼 반복하여 출력한다.
for i in range(len(tables)):
    print("## tables[%s] ##" %i)
    #테이블을 데이터프레임으로 변환한 내용이 여기서 출력됨
    print(tables[i])
    print("="*30)   
    
#두 번째 테이블을 변수에 저장
df = tables[1] 
#name컬럼을 인덱스로 지정한 후 원본에 적용
df.set_index(['name'], inplace=True)
print(df)
print("="*30)   

#웹 URL을 지정
url ='https://pann.nate.com/talk/c20023?page=1'
#테이블을 DF로변환
tables = pd.read_html(url)
#이 페이지에는 테이블이 하나만 있으므로 1이 출력된다.
print('테이블 개수 : ', len(tables))
print("="*30)   

#0번 인덱스로 테이블을 가져온 후 변수에 저장
boardTable = tables[0]  
'''
데이터프레임으로 변환된 테이블의 내용이 출력된다. 
컬럼명은(이미지 태그이기 때문에 분석 불가) Unnamed와 같이 출력된다.
'''
print(boardTable)
print("="*30)

#columns속성을 이용해서 데이터프레임에 컬럼명을 지정한다.
boardTable.columns = ['제목', '작성자', '조회수', '작성일']
print(boardTable)