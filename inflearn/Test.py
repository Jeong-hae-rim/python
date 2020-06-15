'''
변수명 정하기
 1) 영문과 숫자, _ 로 이루어진다.
 2) 대소문자를 구분한다. (인터프리터가 따로 구분한다.)
 3) 문자나, _로 시작한다.
 4) 특수문자를 사용하면 안된다. (&, % 등)
 5) 키워드를 사용하면 안 된다. (if, for 등)
'''

a=1 # 변수 a에다 1를 대입한다.
A=2
A1=3
#2b=4
print(a, A, A1)
a, b, c = 3, 2, 1 #먼저 있던 값이 지워지고 새로운 값이 대입
print(a, b, c)

#값 교환
a, b = 10, 20
print(a, b)
a, b= b, a
print(a, b)


#변수 타입
a=12345
print(type(a)) #<class 'int'>
a=12.1234567899123145656
print(type(a)) #<class 'float'>
a='student'
print(type(a)) #<class 'str'>


#출력 방식
print("number")
a, b, c = 1, 2, 3
print(a, b, c)
print("number : ", a, b, c) #number :  1 2 3
print(a, b, c, sep=', ') #1, 2, 3
print(a, b, c, sep=',') #1,2,3
print(a, b, c, sep='') #123
print(a, b, c, sep='\n') #개행문자 들어가서 한 줄에 한 개씩 출
print(a, end=' ')
print(b, end=' ')
print(c) #1 2 3 위의 두 줄까지 한 
