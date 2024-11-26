'''
for문
    형식] for 반복변수 in 목록형:
        실행문
    range()함수
        : 반복문과 직접적인 연관은 없지만 흔히 반복문과 연동해서 자주 사용하는 함수
        형식]
            range(10) : 0~9까지
            range(2, 10) : 2~9까지
            range(2, 10, 2) : 2~9까지 2씩 증가
'''

for i in range(5):
    print("i=", i, end="  ")
    
print()
print("="*30)

#for문에 list를 사용
list1 = [1,2,3,4,5,6,7,8,9,10]
sum = 0
#리스트의 원소 개수만큼 10번 반복
for i in list1:
    #원소를 누적해서 합산
    sum += i    
print("1부터 10까지의 합 = ", sum)


str1= "파이썬이 좋아요?"
for ch in str1:
    print(ch, end="  ")

print()
print("="*30)

for dan in range(2, 10):
    for su in range(1, 10):
        print("%2d * %2d = %2d" %(dan, su, dan*su), end="  ")
    
    print() 

print()
print("="*30)

for i in range(3):
    print(i, end=" ")
else:
    print("for문 종료됨")
    
print()
print("="*30)

for i in range(3):
    print(i, end=" ")
    break
else:
    print("break를 통해 for문이 완료되지 않았으므로 출력되지 않음")
    
print()
print("="*30)

