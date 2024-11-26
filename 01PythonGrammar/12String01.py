str = 'coffee'
num = 1
#접두어 f를 붙이고, 표현할 변수를 중괄호를 이용해서 삽입한다.
result = f'{str}는 하루에 {num}잔만 마시는게 좋아요'    
print(result)

# 출력 범위 지정 후 정렬. 10칸 정도를 확보한 후 출력할 문자를 정렬한다.
# 남은 공간은 스페이스로 채운다.
str = '문자열 처리' 
result1 = f'{str:<10}'
print(result1)
result2 = f'{str:^10}'
print(result2)
result3 = f'{str:>10}'
print(result3)

#출력 범위 내 정렬 및 문자 채우기. 남은 공간은 하이픈(-)으로 채운다.
result4 = f'{str:-^50}'
print(result4)

#딕셔너리 사용 : Key값으로 접근하여 삽입
dics = {'name':'성유겸', 'gender':'남자', 'age':10} 
result = f'{dics["name"]}은 {dics["gender"]}이고 나이는 {dics["age"]}살이다.'
print(result)

#리스트 사용 : Index로 접근하여 삽입
lists = [10, 20, 30]    
print(f'리스트 : {lists[0]}, {lists[1]}, {lists[2]}')
for v in lists:
    print(f'반복출력 : {v}')