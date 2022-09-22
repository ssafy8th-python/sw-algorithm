# 18870 좌표 압축
# 주소: https://www.acmicpc.net/problem/18870

# 제출한 답
import sys
input = sys.stdin.readline

N = int(input())
n_lst = list(map(int, input().split()))


tmp = sorted(n_lst)
dic = {tmp[0]: 0}
again = 0
for i in range(1, N):
    if tmp[i] == tmp[i - 1]:
        again += 1
    dic[tmp[i]] = i - again

for i in n_lst:
    print(dic[i], end=' ')