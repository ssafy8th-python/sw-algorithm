# 18115 카드 놓기
# 주소: https://www.acmicpc.net/problem/18115

# 제출한 답
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
answer = deque()

for i in range(1, N + 1):
    skill = A[-i]
    if skill == 1:
        answer.appendleft(i)
    elif skill == 2:
        tmp = answer.popleft()
        answer.appendleft(i)
        answer.appendleft(tmp)
    elif skill == 3:
        answer.append(i)

print(*answer)


# 다른 답
import sys
from collections import deque

n = int(sys.stdin.readline())
act = sys.stdin.readline().split()
res = deque()
for i in range(1, n + 1):
    cmd = act.pop()
    if cmd == '1':
        res.appendleft(i)
    elif cmd == '2':
        res.insert(1, i)
    else:
        res.append(i)
print(' '.join(map(str, res)))
