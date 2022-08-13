import sys

sys.stdin = open("input_4843.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    for phase in range(0, N-1):
        minP = phase
        maxP = phase
        if phase % 2:
            for idx in range(phase+1, N):
                if lst[idx] < lst[minP]:
                    minP = idx
            lst[phase], lst[minP] = lst[minP], lst[phase]

        else:
            for idx in range(phase+1, N):
                if lst[idx] > lst[maxP]:
                    maxP = idx
            lst[phase], lst[maxP] = lst[maxP], lst[phase]

    print(f'#{tc}', end=' ')
    print(*lst[:10])



