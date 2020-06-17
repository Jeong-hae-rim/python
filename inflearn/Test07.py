'''
문자열과 내장함수
'''

msg="It is Time"
print(msg.upper()) #모든 글자를 대문자화
print(msg.lower()) #모든 글자를 소문자화
tmp = msg.upper()
print(tmp)
print(tmp.find('T'))
#문자 하나하나 인덱스로 접근할 수 있음
#문자를 찾아 인덱스로 출력하라는 뜻
#순차적으로 찾다 처음 나오는 문자를 출력해줌
print(tmp.count('T'))
#안에 들어있는 글자를 전부 찾아 개수 출력
print(msg[:2])
print(msg[3:5]) #3번 인덱스부터 4번 인덱스까지만 슬라이싱.
print(len(msg))

for i in range(len(msg)):
    print(msg[i], end = ' ')
print()
# 내가 접근하고자 하는 문자열의 길이
# 인덱스로 접근하면 인덱스 내부에 들어있는 문자 하나하나  접근.

for x in msg:
    print(x, end=' ')
print()
# x가 msg 내부에 담겨 있는 문자 하나하나 접근하는 것

for x in msg:
    if x.isupper(): #x가 대문자인 경우
        print(x, end = ' ')
print()

for x in msg:
    if x.islower(): #x가 소문자인 경우
        print(x, end = ' ')
print()

for x in msg:
    if x.isalpha(): #x가 알파벳인 경우
        print(x, end = '')
print()

tmp='AZ'
for x in tmp:
    print(ord(x)) #ord() : 아스키 넘버 출력
    # A의 아스키 넘버 : 65, Z의 아스키 넘버 : 90
    
tmp='az'
for x in tmp:
    print(ord(x))
    # a의 아스키 넘버 : 97, z의 아스키 넘버 : 122

tmp = 66
print(chr(tmp)) #chr() : 숫자에 대응되는 문자를 출력
