# 18111 마인크래프트
# 주소: https://www.acmicpc.net/problem/18111

# 제출한 답
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
# N x N
ground = []
for _ in range(n):
    ground += list(map(int, input().split()))

time = 99999999999999
height = 0
for i in range(0, max(ground) + 1):
    cnt = 0
    tmp_time = 0
    inventory = b
    for j in ground:
        if i > j:
            cnt += (i - j)
            tmp_time += (i - j)
        elif i < j:
            inventory += j - i
            tmp_time += ((j - i) * 2)

    else:
        if cnt > inventory:
            break
        else:
            if time >= tmp_time:
                time = tmp_time
                height = i
                continue
    break

print(time, height)



# 다른 답
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
field = []
for i in range(N):
    field += list(map(int, input().split()))
min_time = 100000000
prev_height = -1
start = min(field)
end = max(field)
while True:
    if end < start:
        break
    mid = (start+end)//2
    sum = 0
    chk = chk_b = 0
    for height in field:
        if mid < height:  # 블럭 부수기(2초)
            sum += (height-mid)*2
            chk_b -= (height-mid)
            chk -= 2
        else:  # 블럭 채우기(1초)
            sum += mid-height
            chk += 1
            chk_b += (mid-height)
    if chk_b > B:
        end = mid-1
        continue

    if min_time > sum or (min_time == sum and prev_height < mid):
        min_time = sum
        prev_height = mid
    if chk <= 0:
        start = mid+1
    else:
        end = mid-1

print(min_time, prev_height)

