# 1. 리스트(list)
my_list1 = [10, '문자열', True]
print(my_list1)
print(type(my_list1)) #<class 'list'>
print(my_list1[1])

# 2. 튜플(tuple)
# 튜플은 수정 불가능(불변, imutable)하고, 읽을 수밖에 없음
my_tuple1 = (1, 2)
print(my_tuple1)
print(type(my_tuple1)) #<class 'tuple'>

# 어떻게 파이썬 내부에서 사용하고 있을까?
my_tuple2 = 1, 2
print(my_tuple2)
print(type(my_tuple2))

x, y = 1, 2
print(x)
print(y)
#이게 튜플이랑 무슨 상관?
#튜플의 경우 애초에 읽기 밖에 못하기 때문에 가능 값을 내부적으로 할당하고 보장함

x, y = y, x
print(x)
print(y)

[1]
#하나의 요소로 구성된 튜플은 값 뒤에 쉼표를 붙여서 만든다.
single_tuple = ('hello',)
print(type(single_tuple))

# 3. range()
# 숫자의 시퀀스를 나타내기 위해 사용하는 함수
print(range(10))
print(list(range(10)))

#a = []
#b = list()