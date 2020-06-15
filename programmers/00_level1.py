# 두 정수 a, b가 주어졌을 때 
# #a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
#예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

def solution(a, b):
    answer = 0
    if a == b:
        answer = a
        print(answer)
    elif a < b:
        answer = sum(range(a, b+1))
        print(answer)
    else:
        answer = sum(range(b, a+1))
        print(answer)

    return answer

solution(6, 10)

# 06 11
# 함수 출력하는 방법을 모르고 있었던 것 같다. 이번 기회에 다시 알 수 있게 되었다.
# input() 함수에 대해서도 어느 정도 알게 되었다.