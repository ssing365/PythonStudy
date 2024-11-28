class Person:
    #생성자 메서드(init). 첫 번째 매개변수로 클래스 자신을 가리키는 self를 기술
    def __init__(self, name, age):
        #멤버변수 정의 및 초기화
        self.name = name
        self.age = age
    #멤버메서드
    #멤버변수 출력용으로 정의
    def showInfo(self):
        print(f"이름 : {self.name}")
        print(f"나이 : {self.age}")
    def justDoit(self, act):
        print(f"{self.name}님이 {act}를 합니다. ")
    # Java의 toString()과 동일하게 인스턴스 변수를 출력할 때 문자열을 반환해준다.
    # def __str__(self):
    #   return f"제 이름은 {self.name}({self.age})입니다."

#인스턴스 생성
person1 = Person('박찬호', 30)
person2 = Person('손흥민', 28)

person1.showInfo()  
person1.justDoit('야구')

'''
toString의 역할을 하는 __str__를 통해 반환된 문자열이 출력된다
만약 이 함수를 정의하지 않으면 인스턴스의 참조값(주소값)이 출력된다.
'''

print(person2)
person2.justDoit('축구')
