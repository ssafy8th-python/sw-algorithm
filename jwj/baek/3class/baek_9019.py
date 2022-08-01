from collections import deque
import sys

for test_cast in range(int(input())):
    register, answer = map(int, input().split()) 
    visit = [False] * 10000
    dslr_deque = deque()

    dslr_deque.append((register, ""))
    visit[register] = True

    while dslr_deque:
        num_register, num_command = dslr_deque.popleft()

        if num_register == answer:
            print(num_command)
            break
        
        D = num_register * 2 %10000
        if not visit[D]:
            # D 2배 %10000
            dslr_deque.append((D, num_command+'D'))
            visit[D] = True

        S = (num_register - 1) % 10000
        if not visit[S]:
            # S -1  -1이면 9999
            dslr_deque.append((S, num_command+'S'))
            visit[S] = True

        L = (num_register * 10 + num_register // 1000) % 10000
        if not visit[L]:
            # L 왼쪽으로 회전
            dslr_deque.append((L, num_command+'L'))
            visit[L] = True

        R = (num_register % 10 * 1000) + num_register // 10
        if not visit[R]:
            # R 오른쪽으로 회전
            dslr_deque.append((R, num_command+'R'))
            visit[R] = True

    
