# 암호생성기
import sys
sys.stdin = open("input (6).txt", "r")


for tc in range(1, 11):
    N = int(input())
    origin_Q = list(map(int, input().split()))
    new_Q = [0]*8
    x = 0
    while True:
        if origin_Q[0] - (x+1) <= 0:
            print(f'#{tc} ', end='')
            print(*origin_Q[1:]+[0])
            break
        for idx in range(0, 7):
            new_Q[idx] = origin_Q[idx+1]
        new_Q[-1] = origin_Q[0] - (x + 1)

        origin_Q = new_Q[::]
        x = (x+1) % 5



'''
N =10
Q = [-1] * N        # 공간 N개만큼 잡음
front = rear = -1
def enqueue(item):
    global rear
    # if rear == N-1:
    #     rear = 0
    rear = (rear + 1) % N   # 원형큐, MOD 연산자
    Q[rear] = item
def dequeue():
    global front
    front = (front + 1) % N
    return Q[front]

'''