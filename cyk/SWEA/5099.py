# 피자굽기
'''
3
3 5
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2
'''

def cheeze(tc, pizza, N):
    q = []
    for idx in range(1, N+1):
        q.append((idx, pizza.pop(0)))

    while len(q) > 1:     # 피자가 하나만 남을때까지
        outIdx, out = q.pop(0)
        if out == 1:
            if pizza:
                idx += 1
                q.append((idx, pizza.pop(0)))
        else:
            q.append((outIdx, out//2))
    print(f'#{tc} {q[0][0]}')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    cheeze(tc, pizza, N)
