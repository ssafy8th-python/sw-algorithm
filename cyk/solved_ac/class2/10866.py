# 덱 구현하기
import sys
input = sys.stdin.readline

result = []
def deque(lst):
    if lst[0] == 'push_front':
        result.insert(0,int(lst[1]))
    if lst[0] == 'push_back':
        result.append(int(lst[1]))
    if lst[0] == 'pop_front':
        if result: # result에 값이 있으면
            a = result.pop(0)
            print(a)
        else:
            print(-1)
    if lst[0] == 'pop_back':
        if result:  # result에 값이 있으면
            a = result.pop(len(result)-1)
            print(a)
        else:
            print(-1)
    if lst[0] == 'size':
        print(len(result))
    if lst[0] == 'empty':
        if result:
            print(0)
        else:
            print(1)
    if lst[0] == 'front':
        if result:
            print(result[0])
        else:
            print(-1)
    if lst[0] == 'back':
        if result:
            print(result[len(result)-1])
        else:
            print(-1)


n = int(input())
for _ in range(n):
    s_input = input().split()
    deque(s_input)