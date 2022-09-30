N, K = map(int, input().split())

dp = [0] * 100001
cnt = [0] * 100001
dp[N] = 1
cnt[N] = 1

q = [N]

while q:
    value = q.pop(0)

    for n_x in (value * 2, value + 1, value -1):
        if 0 <= n_x <= 100000:
            if not dp[n_x]:
                dp[n_x] = dp[value] + 1
                cnt[n_x] = cnt[value]
                q.append(n_x)
            elif dp[n_x] == dp[value] + 1:
                cnt[n_x] += cnt[value]

print(dp[K] - 1)
print(cnt[K])
