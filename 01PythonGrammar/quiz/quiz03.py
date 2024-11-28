'''
문제 3: 소수 판별하기
입력받은 정수가 소수(Prime Number)인지 확인하는 함수를 작성하세요.
(소수: 1과 자기 자신만으로 나누어지는 1보다 큰 정수)
함수 이름: is_prime
입력: 정수 n (예: 7)
출력: True 또는 False
'''
n = int(input("정수를 입력하세요 : "))

def is_prime(n):
    result = True
    
    for i in range(2, n):
        if n%i == 0:
            result = False
            
    return result
    
print(is_prime(n))