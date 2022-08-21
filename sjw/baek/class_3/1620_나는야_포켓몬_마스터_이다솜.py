# 1620 나는야 포켓몬 마스터 이다솜
# 주소: https://www.acmicpc.net/problem/1620

# 제출한 답
import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n: 포켓몬의 수 m: 문제의 수

poke_lst = dict()

for idx in range(1, n + 1):
    tmp = input().rstrip()
    poke_lst[str(idx)] = tmp
    poke_lst[tmp] = str(idx)

for _ in range(m):
    print(poke_lst[input().rstrip()])

    # tmp = input().rstrip()

    # if tmp.isdecimal():
    #     print(poke_lst[int(tmp)])
    # else:
    #     print(poke_lst[tmp])
