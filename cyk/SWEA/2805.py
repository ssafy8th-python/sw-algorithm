import sys
sys.stdin = open("input (2).txt", "r")
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    start = N//2
    end = N//2
    answer = 0

    for i in range(N):
        answer += sum(arr[i][start:end + 1])
        if i < N//2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1

    print(f'#{tc} {answer}')