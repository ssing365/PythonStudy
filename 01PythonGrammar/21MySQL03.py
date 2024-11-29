import pymysql

conn = pymysql.connect(host = 'localhost', user = 'sample_user', 
                       password = '1234', db = 'sample_db', port=3307, charset='utf8')
curs = conn.cursor()

sql = """update board 
        set title='{1}', content='{2}'
        where num = {0}
        """.format(input('수정할 일련번호 : '), input('제목 : '), input('내용 : '))

try : 
    curs.execute(sql)
    conn.commit()
    print("1개의 레코드가 수정됨")
except Exception as e:
    conn.rollback()
    print("쿼리 실행 시 오류 발생", e)
    
conn.close()