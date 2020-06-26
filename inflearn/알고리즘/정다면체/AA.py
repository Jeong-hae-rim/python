import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
cnt = [0]*(n+m+3) # n의 제일 큰 눈과 m의 제일 큰 눈의 합이 index의 최대 크기
max = -2147000000
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1
#print(cnt)
for i in range(n+m+1):
    if cnt[i] > max:
        max = cnt[i]
#print(max)
for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end=' ')



'''

n, m = map(int, input().split())
cnt = []
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt.append(i+j)
        for k in range(1, len(cnt)):
            over = 


처음에 내가 생각했던 로직은 for문을 2중으로 돌린  다음,

미리 생성한 리스트에 요소들을 전부 집어넣고

그 다음 각 요소들의 개수들을 출력해 가장 큰 값만 뽑아내려고 했었다.

근데 for문을 2중으로 돌린 후 append 함수를 써서 미리 생성한 리스트에
넣는 것까지는 성공을 했는데,

그 다음부터는 3중 for문이 되어버리고 중복된 개수를 어떻게 분류할 것인가에
대해 구현할 방법이 막막해져 어려웠었다.

강의를 들은 후 특히

for i in range(1, n+1):

    for j in range(1, m+1):

        cnt[i+j] += 1

이 부분에서



따로 눈의 개수를 더해 리스트에 담고 분류하지 않고

이미 0의 요소로 초기화된 리스트의 인덱스 값에 1개씩 누적한다는 부분은 

새로운 관점으로 문제를 바라볼 수 있게 해주셨다.

'''