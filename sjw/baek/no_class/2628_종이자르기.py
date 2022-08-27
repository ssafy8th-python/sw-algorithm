# 2628 종이자르기
# 주소: https://www.acmicpc.net/problem/2628

# 제출한 답
sero, garo = map(int, input().split())  # 종이 크기
n = int(input())  # 잘라야하는 수

garo_cut = []; sero_cut = []
for _ in range(n):
    check, point = map(int, input().split())
    if check == 0:
        garo_cut.append(point)
    else:
        sero_cut.append(point)
garo_cut.sort()
sero_cut.sort()
garo_len = len(garo_cut)
sero_len = len(sero_cut)

# 가로 중 제일 큰 수 * 세로 중 가장 큰 수
if garo_len != 0:
    max_garo = garo_cut[0]
else:
    max_garo = garo
if sero_len != 0:
    max_sero = sero_cut[0]
else:
    max_sero = sero

for cut in range(garo_len):
    if 0 <= cut - 1:
        max_garo = max(max_garo, garo_cut[cut] - garo_cut[cut - 1])
    if cut == garo_len - 1:
        max_garo = max(max_garo, garo - garo_cut[cut])

for cut in range(sero_len):
    if 0 <= cut - 1:
        max_sero = max(max_sero, sero_cut[cut] - sero_cut[cut - 1])
    if cut == sero_len - 1:
        max_sero = max(max_sero, sero - sero_cut[cut])

print(max_garo * max_sero)


# 수정본
sero, garo = map(int, input().split())  # 종이 크기
n = int(input())  # 잘라야하는 수

garo_cut = []; sero_cut = []
for _ in range(n):
    check, point = map(int, input().split())
    if check == 0:
        garo_cut.append(point)
    else:
        sero_cut.append(point)

garo_cut.append(garo)
sero_cut.append(sero)
garo_cut.sort()
sero_cut.sort()

# 가로 중 제일 큰 수 * 세로 중 가장 큰 수
max_garo = garo_cut[0]
max_sero = sero_cut[0]

for cut in range(1, len(garo_cut)):
    max_garo = max(max_garo, garo_cut[cut] - garo_cut[cut - 1])

for cut in range(1, len(sero_cut)):
    max_sero = max(max_sero, sero_cut[cut] - sero_cut[cut - 1])

print(max_garo * max_sero)
