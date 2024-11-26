'''
퀴즈] 다음과 같은 메트릭스를 출력하는 프로그램을 for문으로 작성하시오.

1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
'''

for i in range(4):
    for j in range(4):
        if(i==j):
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()

'''
퀴즈] 다음과 같은 피라미드를 출력하는 프로그램을 for문으로 작성하시오.

*
**
***
****
*****
'''

for i in range(5):
    for j in range(5):
        if i>=j:
            print("*", end=" ")
    print()