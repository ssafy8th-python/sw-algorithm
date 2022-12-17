# 11660 구간 합 구하기 5
# 주소: https://www.acmicpc.net/problem/11660

# 제출한 답  다시 풀어보기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chartOri = [list(map(int, input().split())) for _ in range(N)]
chartSum = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(N):
        tmpSum = chartOri[i][j] + chartSum[i - 1][j] + chartSum[i][j - 1] - chartSum[i - 1][j - 1]
        chartSum[i][j] = tmpSum

results = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = chartSum[x2 - 1][y2 - 1] - chartSum[x1 - 2][y2 - 1] - chartSum[x2 - 1][y1 - 2] + chartSum[x1 - 2][y1 - 2]
    results.append(result)

for result in results:
    print(result)


# 다른 답
def solution():
    import sys

    input = iter(sys.stdin.read().split("\n")).__next__
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    dp = [before := [0] * (n + 1)] + [      # := 바다코끼리 연산자(대입 표현식, 명명 표현식): 조건문 안에서 선언과 할당을 동시에 하는 방법
        (before := [b := 0] + [
                (b := b + l) + m
                for l, m in zip(line, before[1:])
        ])
        for line in table
    ]
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        x1 -= 1
        y1 -= 1
        print(dp[x2][y2] - dp[x1][y2] - dp[x2][y1] + dp[x1][y1])


solution()