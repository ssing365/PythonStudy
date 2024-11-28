#람다식과 map, filter, reduce 함수 활용
print(f"{'람다식과 map함수1' : -^30}")
multiLambda = lambda x: x*2
list_data = [1,2,3,4,-1,-2,-5,-10]
result = list(map(multiLambda, list_data))
print("결과1",result)
  
print(f"{'람다식과 map함수2' : -^30}")            
list_data2 = [1,2,3,4,5,6,7,8,9,10]            
strNumLambda = lambda x : '3X' if x%3==0 else x
result = list(map(strNumLambda, list_data2))
print("결과2",result)
              
print(f"{'람다식과 filter함수' : -^30}")
list_data3 = [1,4,9,16,25,46,64,81,100]
result = list(filter(lambda z : z>5 and z<80, list_data3))
print("결과3",result)
              
print(f"{'람다식과 reduce함수' : -^30}")
import functools, operator
sum1 = functools.reduce(lambda i, j: i+j, range(1, 11))     
print("결과4-1", sum1)         

sum2 = functools.reduce(operator.add, range(1,11))
print("결과4-2", sum2)