'''
문제 1: 숫자의 합 구하기
사용자로부터 양의 정수를 입력받아 각 자릿수의 합을 계산하는 함수를 작성하세요.
함수 이름: sum_of_digits
입력: 정수 n (예: 1234)
출력: 각 자릿수의 합 (예: 10)
'''
def sum_of_digits():
    user_input = input("양의 정수를 입력하세요 : ")
    inputList = []
    sum = 0
    for x in user_input:
        inputList.append(x)

    for i in inputList:
        a = int(i)
        sum += a       
    
    print(sum)

sum_of_digits()