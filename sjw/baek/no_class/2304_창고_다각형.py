# 2304 창고 다각형
# 주소: https://www.acmicpc.net/problem/2304

# 제출한 답
import sys
input = sys.stdin.readline

n = int(input())  # 기둥의 수
sticks = [list(map(int, input().split())) for _ in range(n)]
sticks.sort()

maxidx = 0
maxS = sticks[0]
for idx in range(n):
    if sticks[idx][1] > maxS[1]:
        maxS = sticks[idx]
        maxidx = idx


result = 0
frontT = sticks[0]
rearT = sticks[n - 1]

for i in range(n):
    if i <= maxidx and sticks[i][1] >= frontT[1]:
        result += frontT[1] * (sticks[i][0] - frontT[0])
        frontT = sticks[i]

    ri = n - 1 - i
    if ri >= maxidx and sticks[ri][1] >= rearT[1]:
        result += rearT[1] * ((rearT[0] + 1) - (sticks[ri][0] + 1))
        rearT = sticks[ri]
result += maxS[1]

print(result)


# 다른 답1
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
mx = 0
for lst in arr:
    if mx < lst[0]:
        mx = lst[0]
check = [0] * (mx + 1)

for lst in arr:
    check[lst[0]] = lst[1]
st = []
for i in range(0, len(check)):
    if not st:  # 처음 시행
        st.append(check[i])
    else:
        if st[-1] < check[i]:   # st의 마지막 값이 현재 인덱스의 값보다 작다면 st에 현재값 추가
            st.append(check[i])

        else:   # 현재 인덱스의 값이 작다면
            if st[-1] <= max(check[i:]):
                st.append(st[-1])

            else:
                st.append(max(check[i:]))

print(sum(st))


# 다른 답2
import sys


N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
index = sorted(data, key=lambda x: x[1])[-1][0]
data.sort(key=lambda x: x[0])
max_index = data[-1][0]
lst = [0] * (max_index + 1)
for a in data:
    lst[a[0]] = a[1]
s, temp = 0, 0
for i in range(data[0][0], index):
    if lst[i] > temp:
        temp = lst[i]
    s += temp
temp = 0
for i in range(max_index, index, -1):
    if lst[i] > temp:
        temp = lst[i]
    s += temp
s += lst[index]
print(s)
