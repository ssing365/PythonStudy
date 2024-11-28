print(f"{'2개 이상의 반환값을 가진 함수':-^30}")
def min_max(num):
    sum = 0
    for val in num:
        sum += val
    return sum, min(num), max(num)

numbers = (8, 7, 6, 8, 4, 9, 5)
sumval, minval, maxval = min_max(numbers)
print("튜플의 합, 최댓값, 최솟값 : ", sumval, minval, maxval)  

print(f"{'지역변수와 전역변수':-^30}")
#전역변수로 정의
total = 0
def sum(arg1, arg2):
    #함수의 지역변수로 정의
    total = arg1 + arg2
    #전역변수와 지역변수가 충돌하면 항상 우선순위가 더 높은 지역변수가 살아남는다.
    print("지역변수 total = ", total)
    return total # 이 변수는 함수를 벗어나면 메모리에서 소멸됨
#초기값 0이 그대로 출력됨
print("전역변수 total = ", total)
#함수 호출 후 반환값은 30이 출력됨
print("sum(10,20) 호출 후 반환값 =", sum(10,20))



print(f"{'내부함수':-^30}")
#외부함수 정의
def person(name, age):
    #내부함수 정의
    def myName(n):
        print("이름 : %s"%n)
    def myAge(a):
        return "나이 : %s"%a
    #내부함수 호출
    myName(name)
    print(myAge(age))
person('성유겸',13) #외부함수 호출. 전달된 인수는 내부함수로 전달되어 결과 출력됨


#가장 일반적
print(f"{'매개변수1 : 순서 매개변수':-^30}")
def paramFunc1(str1, str2):
    print(str1, str2)
    return
cont = "은 매우 좋은 프로그램입니다"
paramFunc1("Python", cont)

print(f"{'매개변수2 : 키워드 매개변수':-^30}")
def paramFunc2(name, age):
    print("이름 : ", name)
    print("나이 : ", age)
    return
paramFunc2(age=50, name='홍길동')

print(f"{'매개변수3 : 디폴트 매개변수':-^30}")
def paramFunc3(lan="Java"):
    print("내가 좋아하는 언어는 ", lan, "입니다.")
    return
paramFunc3()
paramFunc3("C++")

print(f"{'매개변수4 : 가변 매개변수(튜플)':-^30}")
def paramFunc4(*args):
    print("*args=>", args)
    result = 1
    for a in args:
        result *= a
    return result
print(paramFunc4(1,2,3,4))

print(f"{'매개변수4 : 가변 매개변수(딕셔너리)':-^30}")
def paramFunc5(**man):
    print("**man", man)
    for key in man:
        print(key, "=>", man[key])
paramFunc5(의인="홍길동", 장군="이순신", 임금="세종대왕")
