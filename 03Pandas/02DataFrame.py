# -*- coding: utf-8 -*-
import pandas as pd

'''
데이터프레임(DataFrame)
 : 1차원 배열 형태는 시리즈가 여러 개 모여있는 형태로 2차원 배열과 동일하다.
 R의 데이터프레임을 착안하여 만들어졌다. 
 행과 열로 구성된다.
'''

#딕셔너리의 Key는 컬럼명이 되고 Value는 행으로 변환된다.
#즉 3행 5열의 데이터프레임이 생성된다.
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12],'c4':[13,14,15]}

df = pd.DataFrame(dict_data)
print('타입', type(df))
print('데이터프레임1 \n', df)

print('='*30)   

'''
인덱스와 컬럼명을 지정해서 데이터프레임을 생성한다.
인덱스는 행(Row)이 되고, 컬럼은 열(Column)로 지정된다.
'''
df = pd.DataFrame([[20, '남', '부산'], [17, '여', '서울']],
                  index = ['철수', '영희'],
                  columns=['나이', '성별', '지역'])

print('데이터프레임2 \n',df)
print('index\n', df.index)
print('columns\n', df.columns)

print('='*30)

#변경1 : 인덱스와 컬럼명의 속성을 통해 변경
df.index=['학생1','학생2']
df.columns=['연령','남녀','거주']
print('변경1\n',df)

#변경2 : rename() 함수를 통해 변경
'''
변경된 값을 원본 데이터프레임에 즉시 적용하고 싶다면, inplace(=True) 옵션을 추가한다.
해당 옵션을 생략하면(default : inplace = False) 새로운 복사본 객체를 반환한다.'''
df.rename(columns={'연령':'No', '남녀':'Gender', '거주':'City'}, inplace=True)
df.rename(index={'학생1':'Student1', '학생2':'Student2'}, inplace=True)
print('변경2\n',df)

print('='*30)

'''
요소에 접근하기
loc() : 문자형 인덱스명으로 하나의 행을 선택
iloc() : 정수형 인덱스를 통해 행을 선택
'''
stu1 = df.loc['Student1'] #문자형 인덱스로 인출
stu2 = df.iloc[1] #문자형 인덱스를 부여하더라도 정수형 인덱스는 사용할 수 있다.
print('stu1 \n', stu1)
print('stu2 \n', stu2)

print('='*30)

'''
삭제하기
 : drop() 함수를 통해 행 또는 열을 삭제한다.
 축 옵션
     행 삭제 : axis = 0 혹은 미지정. 즉, 행이 디폴트값
     열 삭제 : axis = 1
 여러개를 동시에 삭제할 때는 리스트 형태로 입력하면 된다.
'''

#축 옵션이 없으므로 첫 번째 행이 삭제됨
df.drop('Student1', inplace=True)
print('삭제후1\n', df)

#Gender라는 행이 없으므로 오류가 발생한다.
#df.drop('Gender')

'''
열(컬럼)에 대한 삭제이므로 축 옵션을 1로 지정한다.
'''
#첫 번째 실행에는 inplace옵션이 없으므로 원본 객체에는 적용되지 않는다.
df.drop('Gender', axis=1)
#두 번째 실행에서 원본 객체에 적용된다.
df.drop('Gender', axis=1, inplace=True)
print("삭제후2\n", df)