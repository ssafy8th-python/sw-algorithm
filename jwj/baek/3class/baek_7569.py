import sys
from collections import deque

M, N, H = map(int, input().split())

tomato_store = []

for j in range(H):
    tomato_frame = []
    for i in range(N):
        tmp_frame = list(map(int, sys.stdin.readline().split()))
        tomato_frame.append(tmp_frame)
    tomato_store.append(tomato_frame)


tomato_dequeue = deque()

tomato_cnt = 0 # 익지 않은 토마토의 수

for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomato_store[z][y][x] == 1:    
                tomato_dequeue.append([z, y, x, 0])        
            elif tomato_store[z][y][x] == 0:
                tomato_cnt += 1

zyx_index = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]

result_cnt = 0

tomato = [0, 0, 0, 0]

if tomato_cnt == 0:
    print(0)
else : 
    while tomato_dequeue:
        tomato = tomato_dequeue.popleft()
        
        for zyx in zyx_index:
            z = tomato[0] + zyx[0]
            y = tomato[1] + zyx[1]
            x = tomato[2] + zyx[2]
            
            if (z >= 0 and z < H) and (y >= 0 and y < N) and (x >= 0 and x < M) and (tomato_store[z][y][x] == 0):
                tomato_cnt -= 1
                tomato_store[z][y][x] = 1
                tomato_dequeue.append([z, y, x, tomato[3] + 1])



    if tomato_cnt != 0 :
        print(-1)

    else : 
        print(tomato[3])



# z, y, x