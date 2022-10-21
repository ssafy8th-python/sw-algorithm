# AC
'''
1
RDD
4
[1,2,3,4]
'''
# R은 뒤집기 D는 첫번째 수 버리기
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    command = list(input().strip())
    n = int(input())
    num = deque(input().strip()[1:-1].split(','))

    if n == 0:
        num = deque()

    count = 0

    for cmd in command:
        if cmd == 'R':
            count += 1
        else:
            if len(num) == 0 :
                print('error')
                break
            else:
                if count % 2:
                    num.pop()
                else:
                    num.popleft()

    else:
        if count % 2:
            print('['+','.join(list(num)[::-1])+']')
        else:
            print('['+','.join(num)+']')


