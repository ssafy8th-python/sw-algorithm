# 병합 정렬
# N//2번째 원소와ㅗ 오른쪽 온소가 먼저 복사되는 경우의 수 출력
def merge(llst, rlst):
    lp = rp = 0
    result = []
    while lp < len(llst) and rp < len(rlst):
        if llst[lp] < rlst[rp]:
            result.append(llst[lp])
            lp += 1
        else:
            result.append(rlst[rp])
            rp += 1
    result.extend(llst[lp:])
    result.extend(rlst[rp:])
    return result
def divd(lst):
    global cnt
    if len(lst) == 1:
        return lst
    mid = len(lst)//2
    left = divd(lst[:mid])
    right = divd(lst[mid:])
    if left[-1] > right[-1]:
        cnt += 1

    return merge(left, right)

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    print(f'#{tc}', end=' ')
    print(divd(lst)[N//2], end=' ')
    print(cnt)
