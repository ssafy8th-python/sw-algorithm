
# N은 학급 수, M은 신청 가능한 인원 수
N, M = map(int, input().split())

team = [[] for _ in range(N+1)]


while True:
    n, m = input().split()
    n = int(n)

    if n == 0:
        break

    if len(team[n]) < M:
        team[n].append(m)

for i in range(1, N+1):
    for j in range(len(team[i])):
        for k in range(j+1, len(team[i])):
            if len(team[i][j]) > len(team[i][k]):
                team[i][j], team[i][k] = team[i][k], team[i][j]
            elif len(team[i][j]) == len(team[i][k]):
                for c_index in range(len(team[i][j])):
                    if team[i][j][c_index] > team[i][k][c_index]:
                        team[i][j], team[i][k] = team[i][k], team[i][j]
                        break
                    elif team[i][j][c_index] < team[i][k][c_index]:
                        break


for i in range(1, N+1, 2):
    for m in team[i]:
        print(i, m)

for i in range(2, N+1, 2):
    for m in team[i]:
        print(i, m)
