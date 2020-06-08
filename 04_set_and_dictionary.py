# 1. set
# 순서가 없는 자료 구조
# 집합의 요소는 unique하다. 중복을 허용하지 않는다.
# 순서가 없으므로 set은 요소의 위치나 삽입 순서를 기록하지 않는다.
# 따라서 set은 인덱싱, 슬라이싱 또는 기타 시퀀스와 유사한 동작을 지원하지 않는다.
# 수학에서의 집합과 동일하게 처리된다.
set_a = {1, 2, 3}
set_b = {3, 6, 9}

print(set_a - set_b) #차집합
print(set_a | set_b) #합집합
print(set_a & set_b) #교집합

set_c = set() # 빈 set을 만들 때

 # set_c = {1, 1, 1} => 출력해보면 {1}만 나옴


# 2. dictionary
dict_a = {} # dict에서 빈 dict를 만들 때는 기본적으로 이쪽을 더 권장 (내부적으로 동작할 때 메모리를 덜 잡아먹음)
print(type(dict_a))
dict_b = dict()
print(type(dict_b))

dict_a = {1: 1, 2:2, 3:3, 1:4} # 키가 겹치면 뒤에 온 키로 덮어 씌워지며 실제로 이렇게 작성해서도 안 됨
print(dict_a)

phone_book = {
    '서울' : '02',
    '경기' : '031'
} #json과 타입이 비슷함

print(phone_book['서울'])

#print(dir(dict))
#print(help(dict))

print(phone_book.values())