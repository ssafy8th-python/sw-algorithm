# 5525 IOIOI
# 주소: https://www.acmicpc.net/problem/5525

# 제출한 답
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()
result, cnt = 0, 0

i = 0

while i <= M - 3:
    if S[i] == 'I' and S[i + 1] == 'O' and S[i + 2] == 'I':
        cnt += 1
        i += 2
        if cnt == N:
            result += 1
            cnt -= 1
    else:
        cnt = 0
        i += 1

print(result)


# 다른 답
N = int(input())
M = int(input())
S = input().replace("II", "IOOI").split("OO")


ans = 0
for s in S:
    if len(s) < 2 * N + 1:
        continue
    if s[0] == "O":
        s = s[1:]
    if s[-1] == "O":
        s = s[:-1]
    ans += (len(s) - (2 * N + 1)) // 2 + 1

print(ans)

