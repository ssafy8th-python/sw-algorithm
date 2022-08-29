# 마인크래프트
'''
3 4 99
0 0 0 0
0 0 0 0
0 0 0 1
'''
# 1. 블록을 제거하여 인벤토리에 넣기 : 2초
# 2. 인벤토리에서 블록을 꺼내 가장 위에 있는 블록 위에 놓기 : 1초
N, M, B = map(int, input().split())     # N개의 줄, M개의 땅 높이, B 인벤토리에 있는 블록의 개수
arr = [list(map(int, input().split())) for _ in range(N)]
lst = sorted(sum(arr, []), reverse=True)
end = max(lst)
res = 100000000000000000
level = 0
while end >= 0:
    temp_B = B
    time = 0
    for elem in lst:
        if elem > end:   # 1번
            time += (elem-end)*2
            temp_B += (elem-end)
        elif elem < end: # 2번
            if temp_B -(end-elem) < 0:
                break
            else:
                time += (end-elem)
                temp_B -= (end - elem)
    else:
        if res > time:
            res = time
            level = end
    end -= 1
print(res, level)