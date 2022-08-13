import sys
sys.stdin = open("input (4).txt", "r")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    s = list(map(int, input().split()))
    # print(s)
    for i in range(len(s)-1,0,-1):
        print(s[i])