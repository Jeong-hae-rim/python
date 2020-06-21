'''
람다 함수
(익명의 함수 / 람다 표현식이라고도 부름.)

def plus_one(x):
    return x+1

print(plus_one(1))

plus_two = lambda x: x+2
print(plus_two(1))
'''

def plus_one(x):
    return x+1


a = [1, 2, 3]
print(list(map(plus_one, a)))
#map(함수 명, 자료)

print(list(map(lambda x: x+1, a)))
#함수에 이름이 없어서 이대로 쓰면 됨
#함수로 호출할 필요 없이 표현식으로 써서 바로 출력 가
