T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    vote_lst = [0] * N
    sports = list(map(int, input().split()))
    committee = list(map(int, input().split()))

    for maxV in committee:
        for idx, value in enumerate(sports):
            if maxV >= value:
                vote_lst[idx] += 1
                break

    maxV = 0
    res = 0
    for idx, value in enumerate(vote_lst):
        if maxV < value:
            maxV = value
            res = idx + 1

    print(f'#{tc} {res}')
