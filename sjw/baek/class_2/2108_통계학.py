import sys

input = sys.stdin.readline  # 입력값이 최대 500,000개에 달하므로 시간 단축을 위해 사용함

n = int(input())

# 카운팅
count = [0] * 8001  # 음수 4000개 + 0 1개 + 양수 4000개
# lst[음수]할 경우 뒤에서부터 시작되는 점을 활용

sumv = 0  # 합을 구할 변수
num_lst = []  # 정수들을 넣을 리스트
for _ in range(n):
    num = int(input())
    num_lst.append(num)  # 리스트에 추가
    count[num] += 1  # num과 일치하는 인덱스에 +1
    sumv += num  # 합

# 최빈값
maxv = -100000  # 음수부터 시작하므로 가장 작은 수를 시작수로 잡음
mode = 0  # 최빈값으로 사용할 변수
cnt = 1  # 두번째로 작은 최대값 판별을 위한 변수

for i in range(-4000, 4001, 1):
    if maxv < count[i]:  # 기존 maxv보다 더 많이 카운트 되었는지 판별
        maxv = count[i]
        mode = i  # count의 인덱스가 곧 그 수를 의미
        cnt = 1  # 새로운 최대값이므로 cnt 초기화
    elif maxv == count[i] and cnt < 2:  # 두번째로 작은 최대값 판별
        mode = i
        cnt = 2  # 두번째로 작은 값 상태

# 정렬
for i in range(-3999, 4001, 1):  # 누적합
    count[i] += count[i - 1]

tmp = [0] * n  # 정렬한 값을 넣을 리스트

for j in range(n - 1, -1, -1):  # 정렬
    count[num_lst[j]] -= 1
    tmp[count[num_lst[j]]] = num_lst[j]

# 산술
print(round(sumv / n))  # round()를 사용해 반올림

# 중앙
print(tmp[n // 2])

# 최빈
print(mode)

# 범위 (최대 - 최소)
print(tmp[-1] - tmp[0])
