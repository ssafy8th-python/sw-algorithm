# 노드의 합
import sys
sys.stdin = open("sample_input.txt", "r")

def sumF(lst, L, idx):
    if idx == L:
        return lst[L]
    lst[idx//2] += lst[idx]
    return sumF(lst, L, idx-1)
T = int(input())
for tc in range(1, T+1):
    node, leaf, L = map(int, input().split())
    lst = [0]*(node+1)
    for _ in range(leaf):
        idx, val = map(int, input().split())
        lst[idx] = val
    idx = len(lst) - 1
    print(f'#{tc} {sumF(lst, L, idx)}')
