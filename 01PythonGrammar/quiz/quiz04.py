'''
문제 4: 문자열 단어 개수 세기
주어진 문자열에서 공백으로 구분된 단어의 개수를 세는 함수를 작성하세요.

함수 이름: count_words
입력: 문자열 s (예: "hello world python")
출력: 정수 (단어 개수)
'''

def count_words():
    count = 0
    s = input("문자열을 입력하세요")
    for x in s:
        if x == ' ':
            count += 1
    print(count+1)

count_words()