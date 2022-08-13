#에라토스테네스의 체
import sys
sys.stdin = open("sample_input.txt", "r")
max =  10**6
arr = [True] * (max+1)
arr[0], arr[1] = False, False

for i in range(2, int(max ** 0.5) + 1): # 시간 & 메모리 단축을 위해 입력 for문 밖으로 뺌
    if arr[i]:  # True인 경우
        mult = 2  # 배수 설정
        while mult * i <= max: # 소수의 배수
            arr[mult * i] = False # 제거
            mult += 1

T = int(input())
for tc in range(1, 1+T):
    D, A, B = map(int, input().split()) # 포함되어야 하는 숫자, A이상 B이하
    cnt = 0
    for i in range(A, B+1):
        if arr[i] and str(D) in str(i):
            cnt += 1
    print(f'#{tc} {cnt}')
    # for idx, elem in enumerate(arr[2:], start=2): # 2부터 시작
    #     if elem: # True인 경우
    #         mult = 2 # 배수 설정
    #         while mult * idx <= B: # 범위 이하일때
    #             arr[mult*idx] = False # 소수(idx)의 배수 전부 False
    #             mult += 1
    #
    # print(arr)