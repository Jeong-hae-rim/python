# 논리 연산자
print('--- and ---')
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print('--- or ---') # 하나만 True여도 True로 출력
#ctrl+D를 누르면 하단 쪽의 같은 단어들을 동시 선택 가능
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print('--- not ---')
print(not True)
print(not 0) #boolean형으로 출력 됐을 때 0은 default가 false이기 때문에

#단축 평가 : 평가가 끝까지 가지 않고 결과가 예상이 되었을 때 그 뒤쪽의 코드는 읽지 않는 것
# 첫 번째 값이 확실할 때, 두 번째 값은 확인하지 않음
# 조건문에서 뒷 부분을 판단하지 않아도 되기 때문에 속도 향상
print('--- 단축평가 ---')
vowels = 'aeiou'
print(('a' and 'b') in vowels) #False? 안에 a는 있고 b는 없다. and니까 b는 없으니 False가 맞는 것 같은데...
print(('b' and 'a') in vowels) #True? 왜지? 마지막까지 판단한 a가 vowels에 있기 때문에 true로 출력함
print('a' and 'b') #b? and라는 것은 둘 다 True여야 함. 앞이 True여도 뒤가 True인지 분간할 수 없기 때문에 뒤에까지 평가함

# and는 둘 다 True일 경우에만 True이기 때문에
# 첫 번째 값이 True라도 뒤의 값이 
print(3 and 5) #5?
print(3 and 0) #0?
print (0 and 3) #3? -> 0 
print (0 and 0) #0? (왼쪽 0)

print(5 or 3) #5? 
print(3 or 0) #3?
print (0 or 3) #3? -> 뒤쪽이 True냐 False냐에 따라 값이 달라짐 
print (0 or 0) #0? (오른쪽 0)

#Containment Test
# in 연산자를 통해 요소가 속해있는 지의 여부를 확인할 수 있다.
print('---in---')
print('a' in 'apple')
print(1 in [1, 2, 3]) #[] : 리스트(배열)라고 함