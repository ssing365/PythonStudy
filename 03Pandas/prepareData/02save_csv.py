import pandas as pd

data = {
    'name' : ['Jerry', 'Riah', 'Paul'],
    'algol' : ["A", "A+", "B"],
    'basic' : ["C", "B", "B+"],
    'c++' : ["B+", "C", "C+"],
}

df = pd.DataFrame(data)
#name컬럼을 인덱스로 지정. 원본 데이터프레임에 즉시 적용
df.set_index('name', inplace=True)
print(df)

df.to_csv("../saveFiles/hakjum.csv")
