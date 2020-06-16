'''
반복문을 이용한 문제풀이
 1) 1부터 N까지 홀수 출력하기
 2) 1부터 N까지의 합 구하기
 3) N의 약수 출력하기

n = int(input())
for i in range(1, n+1):
    print(i)

    
1번 문제

n = int(input())
for i in range(1, n+1):
    if i%2 == 1:
        print(i)

2번 문제

n = int(input())
sum = 0
for i in range(1, n+1):
    sum = sum + i # sum을 0부터 시작해서 i를 더하고 sum에 저장하는 식으로
                  # 계속 바퀴를 돌아 누적을 시키는 것이다.
print(sum)

3번 문제

n = int(input())
for i in range(1, n+1):
    if n%i==0: # n을 어떤 숫자로 나눴을 때 나누어 떨어지면 약수이다.
        print(i, end=' ')
'''
