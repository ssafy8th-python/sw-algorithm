N = int(input())

lst = [[x, input().split()] for x in range(N)]

sort_lst = sorted(lst, key=lambda x: int(x[1][0]))

for x in sort_lst :
    print(' '.join(x[1]))