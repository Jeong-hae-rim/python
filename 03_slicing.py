sample_list = list(range(0, 31))
print(sample_list)
print(sample_list[1:3])
print(sample_list[10:-1]) #10부터 -1 지점까지. 10~29까지 출력됨
print(sample_list[0:len(sample_list):3])
print(sample_list[::3]) # ::3 > 처음부터 끝까지 3스텝으로
print(sample_list[::-1]) 
print(sample_list[1:1])