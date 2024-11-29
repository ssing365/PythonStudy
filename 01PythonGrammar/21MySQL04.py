import pymysql

#함수 정의
def delete_record():
    conn = pymysql.connect(host = 'localhost', user = 'sample_user', 
                       password = '1234', db = 'sample_db', port=3307, charset='utf8')
    curs = conn.cursor()
    #무한루프로 구성
    while True:
        #exit를 입력하는 경우 프로그램 종료
        iStr = input("삭제할 일련번호 (종료하려면 'exit'입력) : ")
        
        #대문자를 입력하더라도 하나의 조건으로 판단하기 위해 소문자로 변경.
        if iStr.lower() == 'exit':
            print("프로그램을 종료합니다.")
            break
        
        sql = f"delete from board where num = '{iStr}'"
        
        try :
            curs.execute(sql)
            conn.commit()
            print("1개의 레코드가 삭제됨")
        except Exception as e:
            conn.rollback()
            print("쿼리 실행 시 오류 발생 : ", e)
    conn.close()
    
delete_record()