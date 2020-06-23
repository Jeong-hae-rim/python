import sys
#sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())
a = list(map(int, input().split()))
res=set()

for i in range(N):
    for j in range(i+1, N):
        for m in range(j+1, N):
            res.add(a[i]+a[j]+a[m])
res=list(res)
res.sort(reverse=True)

print(res[K-1])

'''
a.sort(reverse=True)
print(a[K-1])

for  in :
    
    print(i)

**set() 함수는 중복되는 값을 제거하는 함수이다!
중복을 방지하고 3번 반복하려면 3중 for문을 써야 한다.**

set함수와 3중 for문에 대해 알았다면 쉽게 풀 수 있었던 문제였던 것 같다.
까먹지 말자.
'''