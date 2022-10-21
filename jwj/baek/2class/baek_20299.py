import sys
input = sys.stdin.readline

N, K, L = map(int, input().split())

result = []
cnt = 0

for _ in range(N):
    team = list(map(int, input().split()))

    if min(team) >= L and sum(team) >= K:
        result.extend(team)
        cnt += 1

print(cnt)
print(*result)