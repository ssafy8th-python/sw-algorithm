# 10816 숫자 카드2
# 주소: https://www.acmicpc.net/problem/10816

# 제출한 답
import sys
input = sys.stdin.readline


count = [0] * 20000001

n = int(input())
n_lst = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))

for i in range(n):
    count[n_lst[i]] += 1

for j in range(m):
    print(count[m_lst[j]], end=' ')