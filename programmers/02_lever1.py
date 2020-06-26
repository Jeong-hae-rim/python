arr = [1, 1, 3, 3, 0, 1, 1]

def solution(arr):
    answer = []

    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer

print(solution(arr))

'''
배열을 길이로 변환해 자릿값을 구해서 배열에 넣는 문제...
솔직히 조금 어려워서 다른 인터넷 보고 풀었따...
슬퍼...
'''