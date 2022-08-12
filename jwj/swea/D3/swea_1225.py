from collections import deque

for tc in range(10):
    test_case = int(input())
    q = deque()

    q += list(map(int, input().split()))

    cnt = 1
    while True:
        q[0] -= cnt

        if q[0] <= 0:
            q[0] = 0
            tmp = q.popleft()
            q.append(tmp)
            break

        tmp = q.popleft()
        q.append(tmp)

        cnt += 1

        if cnt == 6:
            cnt = 1

    print(f'#{test_case}', end=' ')

    for num in q:
        print(num, end=' ')
    print()



