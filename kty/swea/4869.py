import sys

sys.stdin = open("input_4869.txt", "r")

def paper(N):
    if N > 1 and memo[N] == 0:
        memo[N] = paper(N-1) + 2 * paper(N-2)
    return memo[N]

memo = [1] + [1] + [0] * 300

T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    N = K // 10

    print(f'#{tc} {paper(N)}')

