'''
정렬하면 뒤의 값들은 자신보다 큼
전체 개수 - 자신의 index를 통해 사용할 로프를 결정할 수 있음
뒤의 index들은 자신보다 크기 때문에 사용 가능

예시
로프의 수 10 20 30 40 50
10kg 씩 나눠 들었을 때 중량 50
20                      80
30                      90
40                      80
50                      50

10일 때 5개의 로프를 사용할 수 있음
20일 때 4개의 로프를 사용할 수 있음
30일 때 3개의 로프를 사용할 수 있음
=>
'''

N = int(input())

# 값이 들어가 있는 리스트
arr = []

# input 받은 숫자의 개수를 count 할 리스트
rope = [0] * 10001

# counting 정렬할 리스트
tmp = [0] * N

for _ in range(N):
    num = int(input())
    arr.append(num)
    rope[num] += 1

# 리스트에 들어가 있는 개수
for idx in range(1, 10001):
    rope[idx] += rope[idx-1]

# max 값 0번째 배열의 값으로 초기화
maxV = arr[0]

# 해당하는 인덱스에 값 저장
for num in arr:
    tmp[rope[num]-1] = num
    rope[num] -= 1


for idx in range(N):
    sumV = tmp[idx] * (N - idx)     # 총 로프의 수 - 현재 index

    if maxV < sumV:
        maxV = sumV

print(maxV)
