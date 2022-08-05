# 1436 영화감독 숌
# 주소: https://www.acmicpc.net/problem/1436

# 제출한 답
n = int(input())

sixs = []
num = 0
while len(sixs) < n:
    if '666' in str(num):
        sixs.append(int(num))
    num += 1
print(sixs[-1])