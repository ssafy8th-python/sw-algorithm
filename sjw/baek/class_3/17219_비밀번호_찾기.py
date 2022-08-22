# 17219 비밀번호 찾기
# 주소: https://www.acmicpc.net/problem/17219

# 제출한 답
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

site_dict = dict()

for _ in range(n):
    sites_pw = list(input().split())
    site_dict[sites_pw[0]] = sites_pw[1]


for _ in range(m):
    print(site_dict[input().rstrip()])

