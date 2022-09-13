def inorder(n):
    global cnt
    if n <= N:
        inorder(n * 2)
        arr[n] = cnt
        cnt += 1
        inorder(n * 2 + 1)


T = int(input())

for test_case in range(1, T+1):

    N = int(input())

    arr = [0] * (N + 1)

    cnt = 1

    inorder(1)

    print(f'#{test_case} {arr[1]} {arr[N//2]}')
