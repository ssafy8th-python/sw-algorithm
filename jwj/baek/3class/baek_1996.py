T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    doc = M
    cnt = 0
    while True:
        first = q[0]
        if first == max(q):
            q.pop(0)
            cnt += 1
            if doc == 0:
                break
            else:
                doc -= 1

        else:
            back = q.pop(0)
            q.append(back)

            if doc == 0:
                doc = len(q)-1
            else:
                doc -= 1
    print(cnt)