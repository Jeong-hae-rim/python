import random
import requests


numbers = range(1, 46)
pick = random.sample(numbers, 6)
print(pick)

lotto_url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=914'

response = requests.get(lotto_url)
lotto_info = response.json()

print(type(response.json()))

bonus_num = lotto_info.get('bnusNo')
print(bonus_num)

winner = []

for i in range(1, 7):
    winner.append(lotto_info.get(f'drwtNo{i}'))

print(winner[0:7:1])

#pick, winner 비교해서 pick이 몇 등에 당첨되었는지 확인해보기

match_num = set(pick) & set(winner)
print(len(match_num))

if len(match_num) >= 6:
    print