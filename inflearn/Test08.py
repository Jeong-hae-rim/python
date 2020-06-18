'''
리스트와 내장함수(1)


# 리스트를 만드는 방법

a = []
print(a)

b = list()
print(b)

'''
import random as r


a = [1, 2, 3, 4, 5]
#print(a)
#print(a[0])

b= list(range(1, 11))
#print(b)

c = a + b
#print(c)


print(a)
a.append(6) # 리스트 맨 뒤에 추가하는 함수
print(a)

a.insert(3, 7) # 3번 인덱스 뒤에 7을 추가해주는 함수
print(a)

a.pop()
print(a) # 인자 없이 출력하면 리스트의 맨 뒤에서 하나를 꺼낸다.

a.pop(3)
print(a) #  인자를 주고 출력하면 그 자리의 인덱스가 사라진다.


a.remove(4)
print(a) #4가 제거되고 뒤의 인덱스가 앞으로 차례대로 채워짐

print(a.index(5)) #인자의 인덱스 값을 출력해줌



a = list(range(1, 11))
#print(a)
print(sum(a)) #sum() : 전부 더해주는 함수
print(max(a)) #max() : 리스트 내에서 가장 큰 수를  출력
print(min(a)) # min() : 리스트 내에서 가장 작은 수를 출력
print(min(5, 7)) # 인자 값들 중에서 최소를 찾아주는 함
print(min(5, 3, 7)) # 순서 상관 없이 찾아내서 출력해준다


print(a)

r.shuffle(a)
print(a) # random.suffle() : 인자들의 순서를 마구잡이로 섞어 출력
         # r? >> as r을 해줬기 때문에  별명을 붙여준 셈

a.sort(reverse=True) # 내림차순 정렬
print(a) 


a.sort() # 오름차순 정렬
print(a)

a.clear() # a list 안의 값들이 전부 제거되고 빈 리스트만 출력
print(a)
