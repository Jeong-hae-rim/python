'''
조건문 if (분기, 중첩)

x=15
if x>=10: # == : 같다. 관계 연산자. !=  같지 않다.
    print("Lucky") #4칸 들어가면 이 줄은 if문에 속한다.
    print("ㅋㅋ")


x=10
if x>0:
    if x<10:
        print("10보다 작은 자연수")

x=7
if x>0 and x<10:
        print("10보다 작은 자연수")

x=7
if 0<x<10:
        print("10보다 작은 자연수")

x=-3
if x>0:
    print("양수")
else:
    print("음수")
'''

x=50
if x>=90:
    print('A')
elif x>=80:
    print('B')
elif x>=70:
    print("c")
elif x>=60:
    print("D")
else:
    print("F")
