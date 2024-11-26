#3개의 정수형 변수 선언
#산술연산자
x=2
y=4
z=8

print("x + y", x+y)
print("x - y", x - y)
print("x * y", x * y)
#나누기 연산, 결과는 실수(float)형으로 반환.
print("x / y", x / y)
#몫을 구하기 위한 나누기 연산, 결과는 정수 (int)형을 반환.
print("x // y", x // y)
#거듭제곱. 즉 x의 y승의 결과 반환.
print("x ** y", x ** y)
#pow(): 파이썬에서 제공하는 기본함수. 거듭제곱의 결과 반환
print("pow(x, y)", pow(x, y))
#x의 y승의 결과를 z로 나눈 나머지가 반환됨.
print("pow(x, y, z)", pow(x, y, z))
#x를 y로 나눈 몫과나머지를 Tuple로 반환함.
print("divmod(x, y)", pow(x, y))

'''
수학 관련 여러가지 함수를 가지고 있는 math모듈을 현재 문서에 
import한 후 팩토리얼 함수를 호출
'''

import math
print("math.factorial(5)", math.factorial(5))

