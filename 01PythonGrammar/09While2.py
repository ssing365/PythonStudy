'''
시나리오] 1부터 20까지 숫자 중 홀수만 출력하는 프로그램을 작성하시오.
conutinue 사용
'''

a = 1
while a<=20:
    if a%2==0:
        a += 1 #짝수인 경우 단순히 1 증가
        continue
    else:
        print(a, end=' ') #반복문 안에서 만나 
        a += 1

print()
print("="*30)

#시나리오] 구구단 출력
dan = 2
while dan<=9:
    su = 1
    while su <= 9:
        print("%d*%d=%2d" %(dan, su, dan*su), end=" " )
        su += 1
    dan += 1
    print()

print()
print("="*30)

#시나리오] 구구단 짝수단만 출력
dan = 2
while dan<=9:
    if dan%2 == 1:
        dan += 1
        continue
    else:
        su =1
        while su<= 9:
            print("%d*%d=%2d" %(dan, su, dan*su), end=" " )
            su += 1
    dan += 1
    print()
    
print()