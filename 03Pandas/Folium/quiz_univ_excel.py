# -*- coding: utf-8 -*-
"""
‘전문 및 대학교 현황’ 에서 다운로드 한 엑셀 데이터를 g_univ 테이블에 insert 하는 프로그램을 작성하시오. 
"""
import cx_Oracle as cx
import pandas as pd

#확장자가 xlsx가 아닌 xls라면 xlrd 라이브러리 설치 => conda install xlrd
df = pd.read_excel('../resData/전문및대학교현황.xls', engine='xlrd')

df.head()
df.info()

host_name ='localhost'
oracle_port = 1521
service_name = 'xe'
connect_info = cx.makedsn(host_name, oracle_port, service_name)
conn = cx.connect('education', '1234', connect_info)
cursor = conn.cursor()

#for문으로 데이터프레임 인덱스 접근 방법 : iterrows()를 사용
for index, row in df.iterrows():
    print(row['시군명'], row['시설명'], row['소재지도로명주소'], row['WGS84위도'], row['WGS84경도'])
    print(type(row['WGS84위도']))
    print(index)
    
    SIGUN_NM = row['시군명']
    FACLT_NM = row['시설명']
    REFINE_LOTNO_ADDR = row['소재지도로명주소']
    REFINE_WGS84_LAT =  row['WGS84위도']
    REFINE_WGS84_LOGT = row['WGS84경도']
    
    sql = "insert into g_univ (idx, sigun, faclt, addr, latitude, longitude)  \
        values (MYBOARD_SEQ.nextval, :sigun, :faclt, :addr, :latitude, :longitude)"
        
    try:
        cursor.execute(sql, sigun=SIGUN_NM, faclt=FACLT_NM, addr=REFINE_LOTNO_ADDR,
                       latitude=REFINE_WGS84_LAT, longitude=REFINE_WGS84_LOGT)
        conn.commit()
        print("1개의 레코드 입력")
    except Exception as e:
        conn.rollback()
        print("insert 실행시 오류 발생", e)
        
conn.close()