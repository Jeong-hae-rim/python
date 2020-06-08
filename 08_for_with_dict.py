classroom = {
    'teacher': 'kim',
    'student1': 'hong',
    'student2': 'choi'
}

for member in classroom:
    print(member) # key

for member in classroom:
    print(classroom[member]) # value

#keys
for member in classroom.keys():
    print(member) 
# 1번 for문과 3번 for문 중 직관적으로 어떻게 동작하는지 알아볼 수 있는 for문은 3번이다.

# values
for member in classroom.values():
    print(member) 
# 이 또한 마찬가지이다.

# items
for key, value in classroom.items():
    print(key, value)
# key와 value의 쌍은 클래스 타입이 튜플이다.