import requests, json
import pandas as pd

df = pd.read_csv('../resData/경기도공공배달앱배달특급가맹점.csv', encoding='cp949')
df.info()

url = "https://openapi.gg.go.kr/GGEXPSDLV"
params = dict(
    Type = 'json',
    pSize ='1000',
    pIndex = '36',
    KEY = 'c7978714eb6c4d99b856ffdf6718b0e2'
)
raw_data = requests.get(url=url, params=params)
json_data = raw_data.json()

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
    print(SIGUN_NM,STR_NM,BIZREGNO,REFINE_ROADNM_ADDR,REFINE_LOTNO_ADDR,
          INDUTYPE_NM,REFINE_ZIPNO,REFINE_WGS84_LAT,REFINE_WGS84_LOGT)
