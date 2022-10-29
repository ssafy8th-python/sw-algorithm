# 1991 트리 순회
# 주소: https://www.acmicpc.net/problem/1991

# 제출한 답
import sys
input = sys.stdin.readline


def VLR(node):
    if node >= 0:
        print(chr(node + ord('A')), end='')
        VLR(tree[node][0])
        VLR(tree[node][1])


def LVR(node):
    if node >= 0:
        LVR(tree[node][0])
        print(chr(node + ord('A')), end='')
        LVR(tree[node][1])


def LRV(node):
    if node >= 0:
        LRV(tree[node][0])
        LRV(tree[node][1])
        print(chr(node + ord('A')), end='')


N = int(input())
tree = [0] * 27
for i in range(N):
    P, L, R = input().strip().split()
    tree[ord(P) - ord('A')] = [ord(L) - ord('A'), ord(R) - ord('A')]

VLR(0)
print()
LVR(0)
print()
LRV(0)
