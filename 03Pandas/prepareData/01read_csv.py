# -*- coding: utf-8 -*-
'''
CSV(Comma-separated values)
 : 텍스트 파일의 일종으로, 콤마로 열을 구분하고 엔터로 행을 구분한다.
 엑셀로 주로 생성한다.
'''
import pandas as pd
file_path = '../resData/sample.csv'

'''
read_csv() 
: CSV파일을 데이터프레임으로 변환한다.
별도의 옵션이 없으면 첫 번째 행을 컬럼으로 간주한다.
그리고 행은 정수형으로 지정된다.
'''
df1 = pd.read_csv(file_path)
print(df1)
print('마지막 데이터', df1.loc[2, 'c3'])
print("=" * 30) 

'''
header옵션 : 컬럼명으로 사용될 행의 번호를 지정한다. 기본값은 0.(즉, 첫 행이 컬럼명이 됨)
    첫(0)행부터 데이터가 있다면 None으로 지정하면 된다. 이 경우 컬럼은 정수형이 지정된다.
'''
df2 = pd.read_csv(file_path, header=None)
print(df2)
print('마지막 데이터', df2.iloc[3,3])
print("=" * 30) 

'''
index_col : 행의 인덱스로 사용할 열의 번호를 지정한다.
    header옵션이 없으므로 첫 행은 컬럼명으로 지정된다.
'''
df3 = pd.read_csv(file_path, index_col=None)
print(df3)
print('마지막 데이터', df3.iloc[2,'c3'])
print("=" * 30) 

'''
c0 컬럼을 인덱스로 지정한다. 
그러면 인덱스로 지정된 컬럼은 데이터에서 삭제된 후 인덱스로 이동한다.
'''
df4 = pd.read_csv(file_path, index_col='c0')
print(df4)
print('마지막 데이터', df4.loc[2,'c3'])
print("=" * 30) 

'''
names 옵션을 통해 열의 이름으로 사용할 문자열 리스트를 설정할 수 있다.
'''
df5 = pd.read_csv(file_path, names=['삼장법사', '손오공', '저팔계', '사오정'])
print(df5)
print('마지막 데이터', df5.loc[3,'사오정'])
print("=" * 30) 

'''
names 옵션으로 컬럼을 지정할 때 리스트 요소 수가 데이터의 개수보다 적으면 끝에서부터 맞춰 지정된다.
즉c0는 인덱스가 되고, c1~c3까지 데이터가 된다.
'''
df6 = pd.read_csv(file_path, names=['유비', '관우', '장비'])
print(df6)
print('마지막 데이터', df6.loc[2,'장비'])
print("=" * 30) 

#skiprows : 처음 몇 줄을 skip할지 설정한다.
df7 = pd.read_csv(file_path, skiprows=2)
print(df7)
print('마지막 데이터1', df7.iloc[0, 3])
print('마지막 데이터2', df7.loc[0, '8'])