import sys
#sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
cnt  = 0

for i in range(1, n+1):
    if n%i == 0:
        cnt+=1
    if cnt == k:
        print(i)
        break
else:
    print(-1)


'''
def aliquot(n, k):
    for i in range(1, n+1):
        if n%i==0:
            if k <= n:
                print()
            else:
                print(-1)


aliquot(6,3)

감상평 : 너무 어렵게 생각했던 거 같다.
나는 i를 리스트에 다시 넣어서 i 리스트의 k번째를 꺼내면 된다고
생각을 했었는데, 저렇게 개수로 저장을 해서,
개수에 맞는 i 값을 꺼내오는 방법도 있었다.

'''