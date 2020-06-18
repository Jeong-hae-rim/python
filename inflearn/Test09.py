'''
리스트와 내장함수(2)
'''

a = [23, 12, 36, 53, 19]
print(a[:3]) #  a[:i] 시작이 없으면 0번부터  i-1번까지의 인덱스를 출력
print(a[1:4]) # a[i:j] 시작이 있으면 i번부터 j-1번까지의 인덱스를 출력
print(len(a)) # len() : 리스트의 길이를 출력해주는 함수

for i in range(len(a)):
    print(a[i], end=' ') #for문으로 인덱스 하나하나 접근해보는 것
print()

for x in a:
    print(x, end=' ') #위의 코드와 결과물은 같음 하나하나 리스트의 원소에 접근 가
print()


for x in a:
    if x%2==1:
        print(x, end=' ') 
print()

for x in enumerate(a): #enumerate() : 인덱스와 원소를 튜플 형태로 출력해주는 함수
    print(x) #(0, 23), (1, 12), (2, 36), (3, 53), (4, 19)

#튜플이란?
b=(1, 2, 3, 4, 5)
print(b[0])
#b[0] = 7 #리스트는 새로 값을 대입 가능한데 튜플은 절대 불가능함
#print(b[0]) #TypeError: 'tuple' object does not support item assignment


for x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value) #index와 원소값을 동시에 접근 가능한 함수가 enumerate()함수이다.
print()

if all(50>x for x in a): #all() : 안의 조건이 모두 참이어야 True 출력
    print("YES")
else:
    print("NO") #하나라도 거짓되는 값이 나오면 바로 else 값 출력

if any(11>x for x in a): #any() : 안의 조건이 한 번이라도 참이면 True 출력
    print("YES")
else:
    print("NO") #모두가 거짓이어야 else값 출력
