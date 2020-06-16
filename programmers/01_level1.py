'''
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, 
solution을 완성해주세요.
'''

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            answer = answer + i
        else:
            continue
    return answer

'''
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

다른 사람의 코드 중 제일 잘 짰다고 칭찬 받는 코드.
컴프리헨션을 사용해 1줄로 줄인 코드.
반을 넘을 때는 계산할 필요가 없기 떄문에 성능이 향상된다고 한다.
num/2 의 값들을 검사해서 리스트에 배열로 넣은 뒤 sum 함수로 더해버리는 방법을
사용한 것 같다.
대단하다.
'''
