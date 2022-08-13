import sys
sys.stdin = open("sample_input (5).txt", "r")

T = int(input())
for tc in range(1, 1+T):
    D, A, B = map(int, input().split())
    for i in range(A,B+1):
        cnt = 0
        for j in range(2,i+1):
            if i % j == 0:
                cnt += 1
        if cnt == 1