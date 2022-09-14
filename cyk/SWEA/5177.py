# 이진 힙
'''
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40
'''
def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c //2
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2
T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    lst = list(map(int, input().split()))
    heap = [0] * (n+1)
    last = 0
    for elem in lst:
        enq(elem)
    res = 0
    asc = n
    while asc > 0:
        res += heap[asc//2]
        asc = asc // 2
    print(f'#{tc} {res}')