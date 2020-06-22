import sys
sys.stdin = open("input.txt", "rt")

T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))

'''
    s가 2고 e가 5라면 2번째 자리부터 5번째 자리이기 때문에
    인덱스 번호로 따졌을 때 인덱스는 0부터 시작하므로
    s는 1이고 e는 4이다.
    그래서 s에서 -1을 해주어야 하고 e는 그대로 써주면 
    그 이전 자리까지 출력하므로
    a[s-1:e]인 것이다.

    2가 먼저 T에 들어오고
    그 다음 줄이 n, s, e, k로 들어오고
    그 다음 줄이 a에 리스트로 들어오는 것까지는 이해했다.
    
    이게 2번 반복한단 의미고

    sort를 해서 오름차순으로 정렬해준 뒤 print를 해줘야 한다는 것을 이해했다.

    %d는 정수형 서식이다!
    print("#%d %d" %(t+1, a[k-1]))
    %d라는 문자 안에 뒤에있는 정수가 입력돠는 형식

    잘 모르는 부분은 정리해서 강사님한테 여쭤보자.
'''