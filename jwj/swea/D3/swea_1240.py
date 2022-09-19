T = int(input())

for test_case in range(1, T+1):

    N, M = map(int, input().split())

    secret = {
    '0001101':0, '0011001':1, '0010011':2, '0111101':3, 
    '0100011':4, '0110001':5,'0101111':6, 
    '0111011':7, '0110111':8, '0001011':9}

    arr = [input() for _ in range(N)]

    check = False
    for i in range(N):
        for j in range(M-7):
            if secret.get(arr[i][j:j+7], 'f') != 'f':
                check = True
                break

        if check:
            break

    col = i
    row = j
    cnt = 0

    result = []
    while cnt < 8:
        val = secret.get(arr[col][row:row+7], 'f')
        if val != 'f':
            result.append(val)
            cnt += 1
            row += 7
        else:
            result = []
            cnt = 0
            j += 1
            row = j

    left = 0
    right = 0

    for idx in range(len(result)):
        if idx % 2:
            right += result[idx]
        else:
            left += result[idx]

    is_true = left * 3 + right

    print(f'#{test_case} {0 if is_true % 10 else sum(result)}')
