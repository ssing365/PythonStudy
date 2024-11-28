'''
모듈 : 다른 파이썬 프로그램에서 불러와 사용할 수 있도록 만든
    파이썬 파일로 변수 혹은 함수 등을 모아놓은 것이다.
'''

#방법1 : 모듈명만 임포트. 이 경우 모듈명을 함께 기술해서 함수를 호출한다.
import mod1
print("모듈의 함수호출1 : ", mod1.add(3,4))
print("모듈의 함수호출2 : ", mod1.sub(4,2))

#방법2 : 이와 같이 하면 함수 호출 시 모듈명을 생략할 수 있다.
from mod1 import add
result = add(3,4)
print("결과 : ", result)

#방법3 : 방법2와 동일하지만 모든 함수를 한꺼번에 임포트하는 방식
from mod1 import *
result1 = add(3,4)
print("결과 : ", result1)
result2 = sub(3,4)
print("결과 : ", result2)

#__name__변수를 사용하여 작성된 모듈 임포트
import mod2
#임포트하면 __name__에는 mod2가 저장된다.
result = mod2.mul(3,4)
print(result)

#모듈을 나눠서 관리할 때는 패키지를 사용한다.
import commons.mod3
#패키지명까지 포함한 형태로 함수 호출
commons.mod3.sum1To10()

#함수명 만으로 호출
from commons.mod3 import sum1To10
sum1To10()