commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
array = [1, 5, 2, 6, 3, 7, 4]

answer = []
for i, j, k in commands:
    arr = array[i-1:j]
    arr.sort()
    a = arr[k-1]
    answer.append(a)
print(answer)

'''
리얼로 내 힘으로 푼 문제!
sort를 해야 하는데 그러려면 2차원 배열의 요소에 접근해야 했다.
2차원 배열에 어떻게 접근해서 풀어야 할까 엄청 골머리 싸맸다.
그러다 이론에서 in 앞에 변수를 n 개 지정해주면 
가로 한 줄(안쪽 리스트)에서 요소 n 개를 꺼내 온다는 거에서
딱 아! 하고 깨달아서 어찌저찌 잘 풀었다.
쾌감...
'''