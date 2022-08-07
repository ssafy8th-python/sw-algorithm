N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]

for i in sorted(lst) :
    print(i[0], i[1])