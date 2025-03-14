'''
문제 2: 팰린드롬 문자열 확인
주어진 문자열이 팰린드롬인지 확인하는 함수를 작성하세요.
(팰린드롬: 앞뒤가 똑같은 문자열, 예: "level", "radar")
함수 이름: is_palindrome
입력: 문자열 s (예: "radar")
출력: True 또는 False
'''
s = input("문자열을 입력하세요 : ")
def is_palindrome(s):
    result = True

    left = 0
    right = len(s)-1

    while left < right:
        if s[left]!=s[right]:
            result = False
        left += 1
        right -= 1
        
    return result
    
print(is_palindrome(s))

#다른 방법
def is_palindrome2(s):
    reverseStr = s[::-1] #''.join(reversed(s))
    result = True
    
    if(reverseStr != s):
        result = False
    
    return result

print(is_palindrome2(s))
        