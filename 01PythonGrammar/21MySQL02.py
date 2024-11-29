#모듈 임포트
import pymysql

#DB연결 : port의 경우 3306이 디폴트 값이므로 변경되지 않았다면 별도로 명시하지 않아도 된다.
conn = pymysql.connect(host = 'localhost', user = 'sample_user', 
                       password = '1234', db = 'sample_db', port=3307, charset='utf8')
curs = conn.cursor()

# f-string을 통해 문자열 중간에 {}를 통해 함수 호출문장을 삽입
sql = f"""insert into board (title, content, id, visitcount)
    values (' {input('제목 : ')}', '{input('내용 : ')}', 'nakja', 0)"""
    
try:
    #쿼리문 실행
    curs.execute(sql)
    #MariaDB에 변경사항 적용
    conn.commit()
    print("1개의 레코드가 입력됨")
except Exception as e:
    #오류가 발생하면 롤백처리
    conn.rollback()
    print("쿼리 실행 시 오류 발생", e)

conn.close()
