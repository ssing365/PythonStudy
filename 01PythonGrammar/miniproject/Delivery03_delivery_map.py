import cx_Oracle as cx
import folium

# 오라클 연결
host_name = 'localhost'
oracle_port = 1521
service_name = 'xe'
connect_info = cx.makedsn(host_name, oracle_port, service_name)
conn = cx.connect('education', '1234', connect_info)
cursor = conn.cursor()

user_input = input("원하는 지역을 입력하세요 : ")
delivery_map = folium.Map(location=[37.40, 127.38], zoom_start=10)

# 수정된 SQL 쿼리 (바인딩 변수 사용)
sql = "SELECT * FROM delivery_apps WHERE sigun_nm LIKE :input ORDER BY idx ASC"
cursor.execute(sql, {'input': f'%{user_input}%'})

for rs in cursor:
    STR_NM = rs[2]
    latitude = rs[8]
    longitude = rs[9]

    # latitude와 longitude가 None이 아닌지 확인
    if latitude is not None and longitude is not None:
        folium.Marker([latitude, longitude], popup=STR_NM).add_to(delivery_map)
        print(STR_NM, latitude, longitude)
    else:
        print(f"위치 정보가 누락된 데이터: {STR_NM}")

delivery_map.save(f'../saveFiles/delivery_map_{user_input}.html')
print("맵이 생성되었습니다.")