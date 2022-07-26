N = int(input())

P = 'IO' * N + 'I'

P_len = len(P)

M = int(input())

S = input()

cnt = 0
result = 0
idx = 0
while True:
    if idx >= M :
        break

    if S[idx:idx+3] == 'IOI':
        cnt += 1
        idx += 2
        if cnt == N:
            result += 1
            cnt -= 1
    else :
        cnt = 0
        idx += 1

print(result)