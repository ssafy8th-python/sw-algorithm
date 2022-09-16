# 1. 배열에 자연수 x를 넣는다.
# 2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.
# 입력에서 0이 주어진 횟수만큼 답을 출력한다. 만일 배열이 비어있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.
# 최소 힙
import sys
input = sys.stdin.readline
n = int(input())
lst = [int(input()) for _ in range(n)]
def enq(v):
    global last
    last += 1
    heap[last] = v
    c = last
    p = c//2
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2

def deq():
    global last
    tmp = heap[1]
    heap[1] = heap[last]
    last -= 1
    p = 1
    c = p*2
    while c <= last:
        if c+1 <= last and heap[c] > heap[c+1]:
            c += 1
        if heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p*2
        else:
            break
    return tmp

heap = [0]*(len(lst)+1)
last = 0

for elem in lst:
    if elem:
        enq(elem)
    elif elem == 0 and last == 0:
        print(0)
    else:
        print(deq())