from copy import deepcopy
import sys
input = sys.stdin.readline


def attack(lst):
    tmp_lst = deepcopy(lst)
    shoot = 0

    # 행 이동 0, 1, 2, 3, 4
    for m in range(N):
        # 동시에 공격
        weight = [1000] * 3
        attack_lst = [[-1, -1] for _ in range(3)]

        for i in range(N-1-m, -1, -1):

            row = N - i - m

            if row > D:
                break

            for h_idx, hunter_idx in enumerate(hunters):

                for j in range(M):
                    # 적이 있을 때 계산
                    if tmp_lst[i][j] == '1':
                        dist = row + abs(hunter_idx - j)

                        if dist <= D and weight[h_idx] >= dist:
                            if weight[h_idx] == dist and attack_lst[h_idx][1] > j:
                                weight[h_idx] = dist
                                attack_lst[h_idx][0] = i
                                attack_lst[h_idx][1] = j
                            elif weight[h_idx] > dist:
                                weight[h_idx] = dist
                                attack_lst[h_idx][0] = i
                                attack_lst[h_idx][1] = j

        for idx, w in enumerate(weight):
            if w != 1000 and attack_lst[idx][0] != -1 and tmp_lst[attack_lst[idx][0]][attack_lst[idx][1]] == '1':
                tmp_lst[attack_lst[idx][0]][attack_lst[idx][1]] = '0'
                shoot += 1

    return shoot


def nCr(N, r, s):
    global result

    if r == 0:
        tmp = attack(arr)

        if result < tmp:
            result = tmp
        return

    for i in range(s, N - r + 1):
        hunters[r-1] = i
        nCr(N, r-1, i+1)


N, M, D = map(int, input().split())

arr = [list(input().split()) for _ in range(N)]

arr.append([0] * M)
hunters = [0] * 3
result = 0

nCr(M, 3, 0)

print(result)