# 최적경로
import sys
sys.stdin = open("input (12).txt", "r")
T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    lst = list(map(int, input().split()))
    c_x, c_y, h_x, h_y = lst[:4]
    lst = lst[4:]
