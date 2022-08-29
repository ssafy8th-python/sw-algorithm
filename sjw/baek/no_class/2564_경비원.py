# 2564 경비원
# 주소: https://www.acmicpc.net/problem/2564

# 제출한 답
garo, sero = map(int, input().split())
n = int(input())
shop = [list(map(int, input().split())) for _ in range(n + 1)]
full = (garo + sero) * 2


for i in range(n + 1):
    if shop[i][0] == 4:  # 동
        shop[i][1] += garo
    elif shop[i][0] == 2:  # 남
        shop[i][1] = garo * 2 - shop[i][1] + sero
    elif shop[i][0] == 3: # 서
        shop[i][1] = garo * 2 + sero * 2 - shop[i][1]

result = 0
for i in range(n):
    result += min(abs(shop[-1][1] - shop[i][1]), full - abs(shop[-1][1] - shop[i][1]))

print(result)
