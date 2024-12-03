# -*- coding: utf-8 -*-
import pandas as pd

#딕셔너리 정의 및 데이터프레임 생성
exam_data = {'국어' : [90, 80, 70],
             '영어' : [98, 89, 95],
             '수학' : [85, 95, 100],
             '체육' : [100, 90, 90]}
df = pd.DataFrame(exam_data, index=['유비', '관우', '장비']) #생성시 인덱스 지정
print(f"{'df전체출력':-^30}")
print(df, '\n')

#행 선택
'''
    loc() : 인덱스명을 기준으로 행을 선택한다. 선택한 모든 범위가 포함된다.
    iloc() : 정수형 위치 인덱스를 통해 행을 선택한다. 마지막 부분은 제외된다. (파이썬 기본 규칙과 동일)
'''
print(f"{'유비':-^30}") 
label1 = df.loc['유비'] #첫 번째 행을 선택해서 출력
print(label1, '\n')
print(f"{'인덱스':-^30}")
position1 = df.iloc[1] #두 번째 행을 선택해서 출력
print(position1, '\n')

#2개이상 선택
'''
행 인덱스를 사용해서 2개 이상의 행을 선택한다. 단, 이 경우 범위가 아니므로 유의해야 한다.
아래 2문장은 동일한 결과를 출력한다.
'''
print(f"{'유비, 장비':-^30}")
label2 = df.loc[['유비','장비']]
print(label2, '\n')
print(f"{'인덱스 0,2':-^30}")
position2 = df.iloc[[0,2]]
print(position2, '\n')

#범위선택
'''
문자형인 경우 ㅇ마지막 부분이 포함되고, 숫자형인 경우 마지막이 제외된다.
'''
print(f"{'유비:장비':-^30}")
label3 = df.loc['유비':'장비']  
print(label3, '\n')
print(f"{'0:2':-^30}")
position3 = df.iloc[0:2] #여기서는 마지막은 제외되어 2개의 행이 출력됨
print(position3,'\n')

#열선택
'''
열을 선택할 때는 대괄호를 사용하거나, 닷(.)을 사용한다.
닷을 사용할 경우 열 이름이 문자형이어야한다.
시리즈 객체를 반환한다.
'''
print(f"{'수학 열':-^30}")
math1 = df['수학']
print(math1, '\n')
print(f"{'영어 열':-^30}")
english = df.영어 #닷으로 선택
print(english, '\n')
print(type(english), '\n')  #타입은 시리즈임을 확인할 수 있다

print(f"{'국어, 체육 열':-^30}")
column1 = df[['국어', '체육']]
print(column1, '\n')
print(type(column1), '\n') #시리즈가 2개 이상 묶였으므로 데이터프레임 타입으로 출력됨


'''
1개의 
'''
print(f"{'수학 열':-^30}")
math2 = df[['수학']]
print(math2, '\n')  
print(type(math2), '\n')