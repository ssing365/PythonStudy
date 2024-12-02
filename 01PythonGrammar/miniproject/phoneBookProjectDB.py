#MariaDB 연결
import pymysql
conn = pymysql.connect(host = 'localhost', user = 'root', 
                       password = 'kosmo1234', db = 'phoneBook_db', port=3307, charset='utf8')
curs = conn.cursor()

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

#연락처 입력
def create():
    print(f"{' 연락처 추가 ':-^30}")
    input_name = input(" >> 이름 : ")
    
    # 중복 확인 쿼리
    check_sql = f"SELECT COUNT(*) FROM phone_book WHERE user_name = '{input_name}'"
    
    try:
        # 중복 확인 실행
        curs.execute(check_sql)
        result = curs.fetchone()
        
        if result[0] > 0:
            print(f"이름 '{input_name}'은(는) 이미 존재합니다. 다른 이름을 입력하세요.")
            return
        
    except Exception as e:
        #오류가 발생하면 롤백처리
        conn.rollback()
        print("쿼리 실행 시 오류 발생", e)
    
    input_phone = input(" >> 전화번호 : ")
    input_address = input(" >> 주소 : ")
    
    try:        
        sql = f"""insert into phone_book (user_name, phone, address) values ('{input_name}', '{input_phone}', '{input_address}')"""
        
        #쿼리문 실행
        curs.execute(sql)
        #MariaDB에 변경사항 적용
        conn.commit()
        print("연락처가 입력되었습니다.")
        
    except Exception as e:
        #오류가 발생하면 롤백처리
        conn.rollback()
        print("쿼리 실행 시 오류 발생", e)
    
#주소록 출력
def print_phoneBook():
    print(f"{' 주소록 전체 조회 ':-^50}")
    
    #연락처가 한 개라도 존재하는지 확인하는 쿼리
    check_sql = f" SELECT COUNT(*) FROM phone_book "
    
    try:
        #연락처가 한 개라도 존재하는지 확인
        curs.execute(check_sql)
        result = curs.fetchone()

        if result[0] == 0:
            print("아직 주소록이 비어있습니다. 연락처를 추가해주세요!")
            return
        
        #쿼리문 작성 및 실행
        sql = "SELECT * FROM phone_book"
        curs.execute(sql)
    
        #select한 모든 레코드 인출
        rows = curs.fetchall()
    
        print(f"{'번호':<5}{'성명':<10}{'전화':<20}{'주소':<20}")
        print("-"*57)
        
        for row in rows:
            num = row[0]
            name = row[1]
            phone = row[2]
            address = row[3]
            print(f"{num:<5}{name:<10}{phone:<20}{address:<20}")
            
    except Exception as e :
        print("쿼리 실행 시 오류 발생", e)
           
#연락처 검색
def search():
    print(f"{' 연락처 검색 ':-^30}")
    input_name = input(" >> 검색할 연락처 이름 : ")
    
    #검색어와 Like를 이용해서 검색결과 인출
    sql = f"""SELECT * FROM phone_book WHERE user_name LIKE '{input_name}' """
    curs.execute(sql)
    result = curs.fetchone()
    
    if result is None:
        print("주소록에 존재하지 않는 이름입니다.")
        return
    
    print(f"{'번호':<5}{'이름':<10}{'전화번호':<20}{'주소':<20}")
    print("-"*57)
    num = result[0]
    name = result[1]
    phone = result[2]
    address = result[3]
    print(f"{num:<5}{name:<10}{phone:<20}{address:<20}")
              
#연락처 수정
def update():
    print(f"{' 연락처 수정 ':-^30}")
    input_name = input(" >> 수정할 연락처 이름 : ").strip()
    
    # 연락처 존재 확인 쿼리
    check_sql = f"SELECT * FROM phone_book WHERE user_name = '{input_name}'"
    
    try:
        # 존재 확인 실행
        curs.execute(check_sql)
        result = curs.fetchall()

        if not result: 
            print(f"'{input_name}'은(는) 주소록에 존재하지 않는 이름입니다.")
            return
        
        print("새로운 이름, 연락처, 주소를 입력하세요")
        new_name = input("새로운 이름 : ")
        new_phone = input("새로운 전화번호 : ")
        new_address = input("새로운 주소 : ")

        sql = f"""update phone_book set user_name='{new_name}', 
            phone='{new_phone}',
            address = '{new_address}'
            where user_name='{input_name}'
            """
            
        curs.execute(sql)
        conn.commit()
        print("연락처가 수정되었습니다.")
        
    except Exception as e:
        conn.rollback()
        print("쿼리 실행 시 오류 발생", e)
    
#연락처 삭제
def delete():
    print(f"{' 연락처 삭제 ':-^30}")
    input_name = input(" >> 삭제할 연락처 이름 : ")
    
    # 연락처 존재 확인 쿼리
    check_sql = f"SELECT * FROM phone_book WHERE user_name = '{input_name}'"
    
    try :
        # 중복 확인 실행
        curs.execute(check_sql)
        result = curs.fetchone()

        if not result:
            print(f"'{input_name}'은(는) 주소록에 존재하지 않는 이름입니다.")
            return
        
        sql = f"delete from phone_book where user_name = '{input_name}'"
        
        curs.execute(sql)
        conn.commit()
        print("1개의 연락처가 삭제되었습니다.")
    except Exception as e:
        conn.rollback()
        print("쿼리 실행 시 오류 발생 : ", e)
       
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
        conn.close()
        break