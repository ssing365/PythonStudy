import cx_Oracle as cx
import requests, json

# 오라클 접속을 위한 정보를 변수로 정의
host_name = 'localhost'
oracle_port = 1521
service_name = 'xe'
# 연결정보를 객체로 정의
connect_info = cx.makedsn(host_name, oracle_port, service_name)
# 커넥션 객체 생성
conn = cx.connect('education', '1234', connect_info)
# 쿼리문 실행을 위한 커서 생성
cursor = conn.cursor()

url = "https://openapi.gg.go.kr/GGEXPSDLV"
KEY = "c7978714eb6c4d99b856ffdf6718b0e2"

for page in range(1, 38):
    params = {
        'Type': 'json',
        'pSize': '1000',
        'pIndex': str(page),
        'KEY': KEY
    }
    try:
        # API 호출
        raw_data = requests.get(url=url, params=params)
        raw_data.raise_for_status()
        json_data = raw_data.json()

        # 데이터 처리
        for jd in json_data['GGEXPSDLV'][1]['row']:
            SIGUN_NM = jd['SIGUN_NM']
            STR_NM = jd['STR_NM']
            BIZREGNO = jd['BIZREGNO']
            REFINE_ROADNM_ADDR = jd['REFINE_ROADNM_ADDR']
            REFINE_LOTNO_ADDR = jd['REFINE_LOTNO_ADDR']
            INDUTYPE_NM = jd['INDUTYPE_NM']
            REFINE_ZIPNO = jd['REFINE_ZIPNO']
            REFINE_WGS84_LAT = jd['REFINE_WGS84_LAT']
            REFINE_WGS84_LOGT = jd['REFINE_WGS84_LOGT']

            print(SIGUN_NM, STR_NM, BIZREGNO, REFINE_ROADNM_ADDR, REFINE_LOTNO_ADDR,
                  INDUTYPE_NM, REFINE_ZIPNO, REFINE_WGS84_LAT, REFINE_WGS84_LOGT)

            sql = """
                insert into delivery_apps (
                    idx, SIGUN_NM, STR_NM, BIZREGNO, REFINE_ROADNM_ADDR, REFINE_LOTNO_ADDR, 
                    INDUTYPE_NM, REFINE_ZIPNO, REFINE_WGS84_LAT, REFINE_WGS84_LOGT
                ) values (
                    delivery_seq.nextval, :SIGUN_NM, :STR_NM, :BIZREGNO, :REFINE_ROADNM_ADDR, 
                    :REFINE_LOTNO_ADDR, :INDUTYPE_NM, :REFINE_ZIPNO, :REFINE_WGS84_LAT, :REFINE_WGS84_LOGT
                )
            """

            try:
                cursor.execute(sql, {
                    'SIGUN_NM': SIGUN_NM,
                    'STR_NM': STR_NM,
                    'BIZREGNO': BIZREGNO,
                    'REFINE_ROADNM_ADDR': REFINE_ROADNM_ADDR,
                    'REFINE_LOTNO_ADDR': REFINE_LOTNO_ADDR,
                    'INDUTYPE_NM': INDUTYPE_NM,
                    'REFINE_ZIPNO': REFINE_ZIPNO,
                    'REFINE_WGS84_LAT': REFINE_WGS84_LAT,
                    'REFINE_WGS84_LOGT': REFINE_WGS84_LOGT,
                })
                conn.commit()  # 커밋
                print(f"{page} 페이지 - 1개의 레코드 입력")
            except Exception as e:
                conn.rollback()  # 롤백
                print(f"insert 실행시 오류발생 (페이지 {page}):", e)
    except Exception as e:
        print(f"페이지 {page}에서 API 호출 오류 발생:", e)

# DB 연결 해제
conn.close()
