'''
반복문(for, while)

a = range(1, 11) #0부터 9까지
print(list(a))

for i in range(1, 11):
    print(i) #기본적으로 줄을 바꿔가며 출력

for i in range(10, 0, -2):
    print(i)

i = 1
while i<=10:
    print(i)
    i = i+1

i=10
while i>=1:
    print(i)
    i=i-1

i = 1
while True:
    print(i)
    if i == 5:
        break # 특정 조건, 무한 반복을 멈추게 하는 데에  쓰인다.
    i+=1

for i in range(1, 11):
    if i%2==0:
        continue #특정 조건에 해당하면 그냥 지나간다.
    print(i)
'''

for i in range(1, 11):
    print(i)
    if i>15:
        break #for 문에서도 쓸 수 있다
else:
    print(11) #for문이 정상적으로 종료하면 else가 나오고,
              #for문이 정상적으로 종료하지 않으면 else는 나오지 않는다.
