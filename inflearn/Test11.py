'''
함수 만들기

def - define


def add(a,b):
    c = a + b
    print(c)    # 함수가 이렇다는 것만 인식

add(3, 2) # 여기가 메인
add(5, 7)

#항상 메인 스크립트 위에다 함수를 작성해야 에러가 나지 않음


def add(a, b):
    c = a + b
    return c

x = add(3, 2)
print(x)

#a하고 b를 더한 결과 값 c를 호출해 반환한다.
# add(3, 2)가 반환한 값을 받는다.
# return은  값을 리턴하고 함수를 종료하는 역할도 함.


def add(a, b):
    c = a + b
    d = a - b
    return c, d #튜플 자료 구조로 여러 값 리턴 가

print(add(3, 2))
'''


def isPrime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True

a = [12, 13, 7, 9, 19]
for y in a:
    if isPrime(y):
        print(y, end=' ')
        
