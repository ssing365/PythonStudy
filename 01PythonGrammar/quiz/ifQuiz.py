'''
퀴즈1. 국영수점수를 입력받아 평균값을 구하고 이를 통해 학점을 출력하는 프로그램을 작성하시오
'''

kor = int(input("국어 점수를 입력하세요 : "))
eng = int(input("영어 점수를 입력하세요 : "))
mat = int(input("수학 점수를 입력하세요 : "))

sum = kor + eng + mat
avg = sum / 3
if(avg >= 90):
    print("A")
elif(avg >= 80): 
    print("B")
elif(avg >= 70):
    print("C")
elif(avg >= 60):
    print("D") 
else:
    print("F")
    
    
'''
퀴즈2. 아이디를 먼저 입력받은 후 user_info 리스트에 등록되었다면 패스워드를 입력받아
일치하는지 확인하는 프로그램 작성. 패스워드는 1234
'''

user_info = ['dd', 'ff']
input_id = input("아이디를 입력하세요 :")
if input_id in user_info:
    input_pw = input("비밀번호를 입력하세요 : ")
    if(input_pw == "1234"):
        print("로그인 성공")
    else:
        print("로그인 실패")
else:
    print("등록되지 않은 아이디입니다.")
    