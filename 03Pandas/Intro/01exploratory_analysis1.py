import pandas as pd

df = pd.read_csv('../resData/auto-mpg.csv', header=None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print("처음 5개 행", "="*30)
print(df.head())
print("마지막 5개 행", "="*30)
df.tail()

#행의 개수, 열의 개수를 튜플로 변환
print("데이터프레임의 모양과 크기", "="*30)
df.shape

#클래스 유형, 행 인덱스, 열의 이름과 개수, 자료형 등을 출력
print("내용 확인", "="*30)
df.info()

print("자료형 확인1", "="*30)
df.dtypes

print("자료형 확인2 - 컬럼 지정", "="*30)
df.mpg.dtypes
df.cylinders.dtypes

print("기술 통계 정보 확인1", "="*30)
df.describe()
print("기술 통계 정보 확인2 - include 옵션 추가", "="*30)
df.describe(include='all')

print("자료의 개수", "="*30)
df.count()
type(df.count())

print("고유값 확인", "="*30)
unique_values = df['origin'].value_counts()
print(unique_values)