#타이틀 출력
print()
print(f"{'  Phone Book  ':★^30}")


#메뉴 출력 함수
def printMenu():
    print()
    print(f"{'  MENU  ':-^30}")
    print("1.연락처 추가")
    print("2.주소록 전체 조회")
    print("3.연락처 검색")
    print("4.연락처 수정")
    print("5.연락처 삭제 ")
    print("6.Phone Book 종료")
    print()

phone_Dict = {}

#주소록 입력
def create():
    print(f"{' 연락처 추가 ':-^30}")
    input_name = input(" >> 이름 : ")
    input_phone = input(" >> 전화번호 : ")
    input_address = input(" >> 주소 : ")
   
    phone_list = []
   
    if input_name in phone_Dict.keys():
        print("연락처에 이미 존재하는 이름입니다.")
        return
   
    phone_list.append(input_name)
    phone_list.append(input_phone)
    phone_list.append(input_address)
    phone_Dict[input_name] = phone_list
   
    print("연락처가 입력되었습니다.")
   
#주소록 출력
def print_phoneBook():
    print(f"{' 주소록 전체 조회 ':-^50}")
   
    if not phone_Dict:
        print("아직 주소록이 비어있습니다. 연락처를 추가해주세요!")
    else:
        print(f"{'번호':<5}{'성명':<10}{'전화':<20}{'주소':<20}")
        print("-"*57)
        num = 1
        for k,v in phone_Dict.items():
            print(f"{num:<5}{k:<10}{v[1]:<20}{v[2]:<20}")
            num += 1
           
#주소록 검색
def search():
    print(f"{' 연락처 검색 ':-^30}")
    input_name = input(" >> 검색할 연락처 이름 : ")
   
    if input_name in phone_Dict.keys():
        print(f"{'번호':<5}{'성명':<10}{'전화':<20}{'주소':<20}")
        print("-"*40)
        print(f"1    {input_name:<10}{phone_Dict[input_name][1]:<20}{phone_Dict[input_name][2]:<20}")
    else:
        print("주소록에 존재하지 않는 이름입니다.")
           
   
#주소록 수정
def update():
    print(f"{' 연락처 수정 ':-^30}")
    input_name = input(" >> 수정할 연락처 이름 : ")
    new_list = []
   
    if input_name not in phone_Dict.keys():
        print("주소록에 존재하지 않는 이름입니다.")
        return
    else:
        print("새로운 이름, 연락처, 주소를 입력하세요")
        new_name = input("새로운 이름 : ")
        new_phone = input("새로운 전화번호 : ")
        new_address = input("새로운 주소 : ")
       
        new_list.append(new_name)
        new_list.append(new_phone)
        new_list.append(new_address)
       
        del(phone_Dict[input_name])
        phone_Dict[new_name] = new_list
       
        print("연락처가 수정되었습니다.")
   
#주소록 삭제
def delete():
    print(f"{' 연락처 삭제 ':-^30}")
    input_name = input(" >> 삭제할 연락처 이름 : ")
   
    if input_name not in phone_Dict.keys():
        print("주소록에 존재하지 않는 이름입니다.")
        return
    else:
        print(input_name, "이(가) 연락처에서 삭제되었습니다.")
        del(phone_Dict[input_name])
       
       
#사용자에게 메뉴 번호를 입력받고 해당 함수를 실행하는 루프
while True:
    printMenu()
    user_input = input("원하는 메뉴 번호를 입력해주세요 : ")
    if user_input == "1":
        create()
    elif user_input == "2":
        print_phoneBook()
    elif user_input == "3":
        search()
    elif user_input == "4":
        update()
    elif user_input == "5":
        delete()
    elif user_input == "6":
        print("이용해 주셔서 감사합니다!")
        break