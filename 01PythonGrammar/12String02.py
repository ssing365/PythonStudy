#문자열 사용
str = '내 이름은 %s입니다.'%'칸'
print("str1=", str)

#리스트 사용
names = ['유비', '관우', '장비']
for n in names :
    print('이름 : %s'%n)
    
#정수 사용
money = 10000
str = '마우스 가격은 %d원입니다.'%money
print(str)

#실수 사용
pi = 3.141592
print("원주율은 %f"%pi)

#변수가 2개 이상일 때
str = '이름 : %s. 나이 :%d'%('홍길동', 99)
print(str)

#변수를 여러개 초기화
phone, age, height = '010-1234-5678', 28, 181.5
str2 = '전화번호:%s, 나이:%d, 키:%f'%(phone, age, height)
print("str2=",  str2)