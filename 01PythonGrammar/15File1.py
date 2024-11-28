'''
open()
    : 파일을 다룰 때 사용하는 내장함수로 첫 번째 인자인 file경로만 필수사항이고 나머지는 옵션이디ㅏ.
    형식] open(파일경로, mode, buffering, encoding)
    
    mode : 파일열기 모드로 w(쓰기), r(읽기), a(추가)가 있고,
        b(2진모드), t(텍스트모드)로 파일의 형식을 지정할 수 있다.
'''

print("\n내파일01.txt 생성")
print("="*30)
print("내파일01.txt")
print("="*30)


# 새로운 파일을 생성하여 반복문으로 내용을 입력한다. wt이므로 쓰기/텍스트모드로 파일을 오픈한다.
f_open = open("./saveFiles/내파일01.txt", mode='wt', encoding='utf-8')
for i in range(1, 21):
    #서식문자를 이용해 문자열을 구성
    data = "%d번째 줄입니다.\n"%i
    #파일에 내용입력
    f_open.write(data)
# 반복문을 통해 입력한 후 파일 객체를 닫아준다.
f_open.close()

###          여기까지 실행되면 파일은 생성된다.            ###

# 파일을 읽기/테스트모드(rt)로 오픈한다. 파일이 없으면 에러 발생
f_read = open("./saveFiles/내파일01.txt", mode='rt', encoding='utf-8')
# 파일의 길이를 알 수 없으므로 무한루프
while True:
    # 파일의 내용을 한 줄씩 읽음
    line = f_read.readline()
    # 더 이상 읽을 내용이 없다면 반복문 탈출
    if not line : break
    # 내용 출력
    print(line)
# 작업을 마쳤다면 자원 해제
f_read.close()

# 기존 파일에 내용을 추가하기 위해 추가/텍스트모드(at)로 오픈
f_add = open("./saveFiles/내파일01.txt", mode='at', encoding='utf-8')
# 한 줄을 추가한다. 개행문자가 없으므로 줄바꿈 처리는 되지 않는다.
f_add.write("추가하는 내용입니다.")
# 필요한 경우 개행문자(\n)를 추가해야한다.
f_add.writelines(["줄바꿈은 되나?\n", "안되면 개행문자를 넣어주세요."])
f_add.write("마지막 라인입니다.")
f_add.close()

print("\n내파일02.txt 생성")
print("="*30)
print("내파일02.txt")
print("="*30)

#자동으로 파일객체를 open/close 할수있게 with~as를 사용한다.
with open("./saveFiles/내파일02.txt", mode='wt', encoding='utf-8') as myfile:
    #15줄의 문장을 입력하면 자동으로 close된다.
    for i in range(1, 16):
        data = "%d라인 입력합니다.\n" % i
        myfile.write(data)  
    
#앞에서 생성된 파일을 읽기 모드로 open한 후 내용을 출력한다.
with open("./saveFiles/내파일02.txt", mode='rt', encoding='utf-8') as myfile:
    line = None
    while line != '':
        line = myfile.readline()
        print(line.strip('\n'))