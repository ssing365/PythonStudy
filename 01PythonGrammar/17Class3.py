'''
멤버변수의 정보은닉을 위해 private(Java)대신 언더바 2개__를 사용한다.
정보은닉이란 멤버변수의 외부 접근을 차단하고, 클래스 내부에서만 접근하도록 처리하는 것을 말한다.
'''

class Computer:
    #생성자
    def __init__(self, name, pwd):
        #외부 접근 허용(public)
        self.name = name
        #외부 접근 차단(private) : 변수 앞에 __를 추가한다.
        self.__pwd = pwd
    #멤버메서드
    def hitKeyboard(self):
        return f'{self.name}로 키보드 작업을 합니다.'
    def clickMouse(self):
        return f'{self.name}에서 마우스를 클릭합니다.'
    #정보은닉 처리된 멤버변수의 접근을 위한 getter / setter 메서드 정의
    def getPwd(self):
        return self.__pwd
    def setPwd(self, pwd):
        self.__pwd = pwd
        
#인스턴스 생성
myCom = Computer('LG Gram', 'qwer1234')

#멤버메서드 호출
print(myCom.hitKeyboard())  
myCom.clickMouse()

#외부접근이 허용되므로 정상적으로 출력됨
print("컴퓨터 이름", myCom.name)

#private이므로 접근할 수 없어 에러 발생
#print("패스워드", myCom.__pwd)
#따라서 getter를 통해 접근하여 출력해야한다.
print("패스워드", myCom.getPwd())

#pwd 값 변경을 위해 setter(setPwd)를 호출
myCom.setPwd("abcd9876")
print("패스워드 변경 후 1", myCom.getPwd())

'''
맹글링 규칙에 의해 정보은닉 처리된 멤버변수는 이름이 변경되므로
아래와 같이 작성했을 때 값을 변경할 수 없다.
또한 에러도 발생하지 않는다.
'''
myCom.__pwd = "xxxxXXXX"
print("패스워드 변경 후 2", myCom.getPwd())

#맹글링규칙. 권장되지 않음
#print("맹글링규칙", myCom._Computer__pwd)