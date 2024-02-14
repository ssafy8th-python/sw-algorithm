# 1421 나무꾼 이다솜
# 주소: https://www.acmicpc.net/problem/1421

# 제출한 답
import sys
input = sys.stdin.readline

N, C, W = map(int, input().split())
trees = [int(input()) for _ in range(N)]

answer = 0
for i in range(1, max(trees) + 1):
    sale = 0
    for tree in trees:
        wood = tree // i
        remain = tree % i
        cost = wood * C
        if not remain:
            cost -= C
        cur_sale = (i * wood * W) - cost
        if cur_sale > 0:
            sale += cur_sale
    answer = max(answer, sale)

print(answer)


# 다른 답
import sys


def adv_input():
    return sys.stdin.readline().rstrip()


N, C, W = map(int, adv_input().split())
woods = {}
for _ in range(N):
    wood = int(adv_input())
    woods[wood] = woods.get(wood, 0) + 1

ans = 0
for i in range(max(woods.keys())):
    money = 0
    for wood in woods:
        if wood < (i + 1): continue
        piece, remain = divmod(wood, (i + 1))

        used = piece * C
        if remain == 0: used -= C

        sell = (piece * (i + 1) * W) - used
        if sell > 0: money += (sell * woods[wood])

    ans = max(ans, money)
print(ans)
