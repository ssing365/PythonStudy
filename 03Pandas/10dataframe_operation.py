import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')

df = titanic.loc[:, ['age', 'fare']]
print(df.head())
print(df.tail())

addition = df + 10
print(addition.head())

exam_data1 = {'이름' : ['서준', '우현', '인아'],
              '국어' : [90, 80, 70],
              '영어' : [98, 89, 95],}
subject1 = pd.DataFrame(exam_data1)

exam_data2 = {'이름' : ['유비', '관우', '장비'],
              '국어' : [1, 2, 3]}
subject2 = pd.DataFrame(exam_data2)
print(subject1 + subject2)
