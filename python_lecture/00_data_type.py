print('Hello, World!')


number = 10
string = '문자열'
bools = True

print(number, string, bools)

# 숫자형 (int, float, complex-복소수)
a = 3
print(type(a)) 
#<class 'int'> : 클래스가 int타입이라는 뜻

#bool
print(type(False)) 
#<class 'bool'> : 클래스가 bool타입이라는 뜻
#0, 0.0, (), [], {}, '', None(값이 없음) -> 얘네는 기본적으로 False로 표현됨


#문자형
greeting = 'hi'
name = 'haerim'
print(greeting, name)
print(type(name)) 
# <class 'str'> : 클래스가 str 타입

#age = input() # input() : 사용자의 입력을 받는 함수
#print(age)
#print(type(age))

print("""
개행 문자 없이
여러 줄을
그대로 출력 가능함.
도움말 작성할 때 주로 사용함.
""")

print(3 * 'hey' + ' yo!')

#중요 string interpolation
name = 'jeong'

#1. %-formatting : 기본적으로 진행되어 오던  string interpolation
print('Hello, %s' % name)

#2. .format() : 3.5 이후로 나온 것. 지금도 많이 사용함.
print('Hello, {}'.format(name))

#3. f-string (Literal String Interpolation) : 3.6+
print(f'Hello, {name}')

pi = 3.141592
print(f'원쥬율은 {pi : .4}. 반지름이 2일 때 원의 넓이는 {pi * 2 * 2}')