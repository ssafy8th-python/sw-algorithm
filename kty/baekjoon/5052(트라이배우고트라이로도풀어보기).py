import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    num_list = list(sys.stdin.readline().rstrip() for _ in range(n))
    sort_num = num_list.sort()
    for i in range(len(num_list)-1):
        if num_list[i+1].startswith(num_list[i]):
            print('NO')
            break
    else:
        print('YES')
