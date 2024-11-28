import sqlite3

conn = sqlite3.connect('./saveFiles/biography.db')
curs = conn.cursor()

#조회1 : 조회된 레코드를 한꺼번에 출력
print(f"{'조회1':-^30}")
curs.execute('select * from people')
print(curs.fetchall())  

#조회2 : 조회된 결과를 한 행씩 출력
print(f"{'조회2':-^30}")
curs.execute('select * from people')
for row in curs.fetchall():
    print(row)
    
#조회3 : 각 컬럼별로 출력
print(f"{'조회3':-^30}")
curs.execute('select * from people')
for(name, job, pay) in curs.fetchall():
    print(name, ':', job, ':', pay)

print("전체 레코드 select 완료")