# 최대힙

def enq(n):
    global last
    last += 1               # 마지막 정점 추가
    heap[last] = n          # 마지막 정점에 key 추가

    c = last
    p = c // 2

    # 부모가 있고 부모 < 자식인경우 자리 교환
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


def deq():
    global last
    tmp = heap[1]
    heap[1] = heap[last]
    last -= 1

    p = 1
    c = p * 2           # 왼쪽 자식 노드

    while c <= last:    # 자식이 하나라도 있으면
        if c + 1 <= last and heap[c] < heap[c + 1]:     # 오른쪽 노드가 존재하고 더 큰 경우
            c += 1

        if heap[p] < heap[c]:                       # 자식이 더크면 교환
            heap[p], heap[c] = heap[c], heap[p]
            p = c                   # 자식을 새로운 부모로 설정
            c = p * 2
        else:                       # 부모가 더 크면 중단
            break

    return tmp

heap = [0] * 100
last = 0

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)

print(heap)

while last:
    print(deq())