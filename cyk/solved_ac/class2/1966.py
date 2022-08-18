# 프린터 큐
'''
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
'''

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    cnt = 0
    while len(q):
        first = q[0]
        if first == max(q):
            if M == 0:
                cnt+=1
                break
            else:
                q.pop(0)
                cnt += 1
                M -= 1
        else:
            back = q.pop(0)
            q.append(back)
            if M == 0:
                M += (len(q)-1)
            else:
                M -= 1
    print(cnt)