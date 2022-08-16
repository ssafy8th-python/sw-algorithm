n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
result=[]
i = 0
while i < len(lst):
    cnt = 0
    for elem in lst:
        if elem != lst[i] and lst[i][0] < elem[0] and lst[i][1] < elem[1]:
            cnt += 1
    result.append(cnt+1)
    i += 1
print(*result)