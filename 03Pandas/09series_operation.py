# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

#첫번째 시리즈 생성
student1 = pd.Series({'국어':100, '영어':80, '수학':90})
print(f"{'학생1':-^30}")
print(student1)

#시리즈 전체 요소에 덧셈 연산 적용
add_stu = student1 + 30
print(f"{'30 더한 후 ':-^30}")
print(add_stu)

#두번째 시리즈 생성. 첫 번째와 순서가 다르고 NaN을 포함하고 있음
student2 = pd.Series({'수학' : 80, '국어':np.nan, '영어':80})
print(f"{'학생2':-^30}")
print(student2)

#시리즈 연산. 인덱스의 순서가 다르지만 판다스가 알아서 정렬 후 연산해줌
addition = student1 + student2 #add()함수로 대체 가능 
subtraction = student1 - student2 #sub()함수로 대체 가능
#NaN은 연산이 불가능하므로, fill_value옵션을 통해 0으로 대체한다.
multiplication = student1.mul(student2, fill_value=0)
division = student1.div(student2, fill_value=0)

#시리즈를 리스트로 묶은 뒤 데이터프레임으로 변환. 이때 라벨인덱스 부여.
result = pd.DataFrame([addition, subtraction, multiplication, division],
                      index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
'''
덧셈과 뺄셈은 NaN이 연산되므로 결과도 NaN으로 저장된다.
곱셈과 나눗셈은 0으로 대체되어 연산된다. 9으로 나눈 결과는 무한대이므로 inf[inity]로 저장된다.
'''
print(f"{'최종 데이터프레임':-^30}")
print(result)
