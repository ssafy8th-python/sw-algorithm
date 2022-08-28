# 2477 참외밭
# 주소: https://www.acmicpc.net/problem/2477

# 제출한 답
k = int(input())
n_lst = [list(map(int, input().split())) for _ in range(6)]

max_w = 0
max_h = 0
m1 = 0
m2 = 0
check = []
for idx in range(6):
    if n_lst[idx][0] == 1 or n_lst[idx][0] == 2:
        max_w = max(max_w, n_lst[idx][1])
    else:
        max_h = max(max_h, n_lst[idx][1])

    if idx + 3 < 6:
        if n_lst[idx][0] == n_lst[idx + 2][0] and n_lst[idx + 1][0] == n_lst[idx + 3][0]:
            m1 = n_lst[idx + 1][1]
            m2 = n_lst[idx + 2][1]
    if idx == 0:
        if n_lst[idx][0] == n_lst[idx + 2][0] and n_lst[idx + 1][0] == n_lst[idx + 5][0]:
            m1 = n_lst[idx][1]
            m2 = n_lst[idx + 1][1]
        elif n_lst[idx][0] == n_lst[idx + 4][0] and n_lst[idx + 1][0] == n_lst[idx + 5][0]:
            m1 = n_lst[idx][1]
            m2 = n_lst[idx + 5][1]
        elif n_lst[idx][0] == n_lst[idx + 4][0] and n_lst[idx + 3][0] == n_lst[idx + 5][0]:
            m1 = n_lst[idx + 4][1]
            m2 = n_lst[idx + 5][1]

print(k * (max_w * max_h - m1 * m2))


# 다른 답
num = int(input())
der = []    # 방향
lenV = []    # 길이
lengths = []  # 전체에서 제외할 너비
max_lengths = []    # 최대 길이

for i in range(6):
    x, y = map(int, input().split())
    der.append(x)
    lenV.append(y)

for i in range(1, 5):
    if der.count(i) == 1:  # 방향이 하나 뿐이라면 최대 길이임
        max_lengths.append(lenV[der.index(i)])  # 최대 길이
        x = der.index(i) + 3  # 제외할 것의 위치는 무조건 다음 세번째에 있음
        if x >= 6:
            x -= 6
        lengths.append(lenV[x])

print(((max_lengths[0] * max_lengths[1]) - (lengths[0] * lengths[1])) * num)
