# 20529 가장 가까운 세 사람의 심리적 거리
# 주소: https://www.acmicpc.net/problem/20529

# 제출한 답
import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    n = int(input())
    MBTIs = list(input().split())
    chosen = [0] * 3
    distances = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            cnt = 0
            for k in range(4):
                if MBTIs[i][k] != MBTIs[j][k]:
                    cnt += 1
            print(MBTIs[i], MBTIs[j], cnt)
            distances.append(cnt)

    distances.sort()
    print(sum(distances[:3]))

import sys
input = sys.stdin.readline


def distance(lst):
    cnt = 0
    for i in range(2):
        for j in range(i + 1, 3):
            for k in range(4):
                if lst[i][k] != lst[j][k]:
                    cnt += 1
                    if cnt >= answer:
                        return answer
    return cnt


def combinations(n, r, s):
    global answer
    if r == 0:
        answer = min(answer, distance(chosen))
    else:
        for i in range(s, n - r + 1):
            chosen[r - 1] = MBTIs[i]
            combinations(n, r - 1, i + 1)


T = int(input())

for _ in range(T):
    n = int(input())
    MBTIs = list(input().split())
    if n > 32:
        print(0)
    else:
        chosen = [0] * 3
        answer = 1e10
        combinations(n, 3, 0)

        print(answer)
