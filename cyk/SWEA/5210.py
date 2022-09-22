import sys
sys.stdin = open("sample_input (7).txt", "r")
T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())        # 컨테이너수, 트럭수
                                            # 최대 M대의 트럭이 편도로 한번만 운행
    w_i = sorted(list(map(int, input().split())), reverse=True)   # 화물의 무게
    t_i = sorted(list(map(int, input().split())), reverse=True)   # 트럭의 적재용량

    # print(w_i, t_i)
    res = []
    pointer = 0

    for i in range(N):
        if pointer >= M:
            break
        if w_i[i] <= t_i[pointer]:
            res.append(w_i[i])
            pointer += 1
    print(f'#{tc} {sum(res)}')
