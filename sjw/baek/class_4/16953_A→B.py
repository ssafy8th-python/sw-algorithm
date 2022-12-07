# 16953 A → B
# 주소: https://www.acmicpc.net/problem/16953

# 제출한 답 1  56ms
import sys
input = sys.stdin.readline


def bfs(a, n):
    global minV
    if minV != -1 or a > B:     # 최소값이 결정된 후에는 모든 함수 종료
        return
    elif a == B:
        minV = n
        return
    else:
        bfs(a * 10 + 1, n + 1)  # 2배인 경우와 1을 가장 오른쪽에 추가하는 경우 모두 실행
        bfs(a * 2, n + 1)


A, B = map(int, input().split())
minV = -1
bfs(A, 1)
print(minV)


# 제출한 답 2  44ms
import sys
input = sys.stdin.readline


def dp(b, n):
    global minV
    if minV != -1 or b < A:     # 최소값이 결정된 후에는 모든 함수 종료
        return
    elif b == A:
        minV = n
        return
    else:
        if not b % 2:           # 목표값에서 시작값으로 줄여나가는 방식으로 시간을 단축
            dp(b // 2, n + 1)   # 나누었을 때 나머지가 0인 경우는 한정되어 있으므로 시간을 단축할 수 있음
        if not (b - 1) % 10:
            dp((b - 1) // 10, n + 1)


A, B = map(int, input().split())
minV = -1
dp(B, 1)
print(minV)
