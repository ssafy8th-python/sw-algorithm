N = int(input())

lst = [list(map(int,input().split())) for _ in range(N)]

print(sorted(lst, key=lambda x :x[1]))

for k in sorted(lst, key=lambda x :x[1]) :
    if 