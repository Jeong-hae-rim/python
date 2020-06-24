import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

ave = round(sum(a)/n)
min = 2147000000 # 왜?
for idx, x in enumerate(a):
    tmp  = abs(x-ave) #거리의 절대값
    if tmp < min:
        min = tmp # 계속해서 더 작은 값을 찾아야하기 때문에
        score = x
        res = idx+1 #0번 인덱스부터 시작하니까
    elif tmp == min:
        if x > score: # x>= score를 하게 되면 같은 경우에도 바꾸게 됨
            score = x
            res = idx+1
print(ave, res)

'''
평균까지는 구했는데 평균과 가장 가까운 수를 구할 방법을 모르겠음.

print(sum(a)/n)
print()
sum = 0
for i in range(len(a)):
    sum += a[i]
    mid = sum/n
    r = round(mid)
print(r)


새로이 알게 된 점
1. round() : 반올림 함수 
2. abs() : 절댓값 구하는 함수

복습할 함수
enumerate()

'''