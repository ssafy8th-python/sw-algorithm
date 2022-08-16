T = int(input())

for tc in range(1, T+1):
    A, B = input().split()

    cnt = 0

    A_len = len(A)
    B_len = len(B)

    idx = 0
    while idx < A_len - B_len + 1:
        if A[idx:idx + B_len] == B:
            cnt += 1
            idx += B_len
            continue

        idx += 1

    result = A_len - (B_len * cnt) + cnt

    print(f'#{tc} {result}')
