class Dog:
    # MyDogList (파스칼 케이스 = 어퍼 카멜 케이스)
    # myDogList (카멜 케이스 = 로우 카멜 케이스)

    kind = 'canine' # 클래스 변수

    def __init__(self, name):
        self.name = name # 인스턴스 변수
        self.tricks = [] # 각자의 리스트로 
 
    def add_trick(self, trick):
        self.tricks.append(trick)



my_dog = Dog('ddolmang') 
your_dog = Dog('namu')

my_dog.add_trick('hello')
your_dog.add_trick('byebye')

print(my_dog.kind) # 자기한테서 없으면 상위로 올라가 있는 값을 사용.
print(your_dog.kind) # 각각의 독립적인 공간이 존재한다.
print(my_dog.name)
print(your_dog.name)

# 절차 지향 Vs 객체 지향
# 데이터가 흘러다니는 것으로 보는 시각 -> 데이터가 중심이 되는 시각으로 변화

# 절차 지향
def greeting(name):
    return f'hello, {name}'

print(greeting, 'harry')

# 객체지향
class Person :
    def __init__(self, name):
        self.name= name

    def greeting(self):
        return f'hello, {self.name}'
        
my_var = Person('harry')
print(my_var.greeting)