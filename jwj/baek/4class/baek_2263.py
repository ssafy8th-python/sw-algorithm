import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def divide(inStart, inEnd, poStart, poEnd):
    if (inStart > inEnd) or (poStart > poEnd):
        return

    root = postOrder[poEnd]

    preOrder.append(root)

    leftNodeNum = index[root] - inStart
    rightNodeNum = inEnd - index[root]

    divide(inStart, index[root] - 1, poStart, poStart + leftNodeNum - 1)
    divide(index[root] + 1, inEnd, poEnd - rightNodeNum, poEnd - 1)


n = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))

index = [0] * (n + 1)

for i in range(n):
    index[inOrder[i]] = i

preOrder = []

divide(0, n-1, 0, n-1)

print(*preOrder)
