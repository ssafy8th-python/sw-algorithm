import sys

sys.stdin = open("input_4861-2.txt", "r")

T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr1 = [input() for _ in range(100)]
    arr2 = list(zip(*arr1)) # 열 정렬

    maxV = 0
    for i in range(100):
        j = 1
        while i+j <= 100:
            for row in arr1: # 행 검사
                if row[i:i+j] == row[i:i+j][::-1]:
                    if maxV < len(row[i:i+j]):
                        maxV = len(row[i:i+j])
            for col in arr2: # 열 검사
                join_col = ''.join(col)
                if join_col[i:i+j] == join_col[i:i+j][::-1]:
                    if maxV < len(join_col[i:i+j]):
                        maxV = len(join_col[i:i+j])

            j += 1

    print(f'#{tc} {maxV}')