# 5639 이진 검색 트리
# 주소: https://www.acmicpc.net/problem/5639

# 제출한 답
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

VLR = []
while True:
    try:
        VLR.append(int(input()))
    except:
        break


def LRV(start, end):
    if start > end:
        return
    else:
        root = end + 1
        for i in range(start + 1, end + 1):
            if VLR[i] > VLR[start]:
                root = i
                break
    LRV(start + 1, root - 1)
    LRV(root, end)
    print(VLR[start])


LRV(0, len(VLR) - 1)
