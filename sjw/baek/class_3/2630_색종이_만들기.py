# 2630 색종이 만들기
# 주소: https://www.acmicpc.net/problem/2630

# 제출한 답
# import sys
# input = sys.stdin.readline

def paper(sr, er, sc, ec, n):
    tmp = arr[sr][sc]
    flag = True

    for i in range(sr, er):
        for j in range(sc, ec):
            if tmp != arr[i][j]:
                flag = False
                break
        else:
            continue
        break

    if flag:
        if tmp:
            result[1] += 1
        else:
            result[0] += 1
        return
    else:
        for r in range(sr, er, n // 2):
            for c in range(sc, ec, n // 2):
                paper(r, r + n // 2, c, c + n // 2, n // 2)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = [0, 0]
paper(0, N, 0, N, N)

for i in result:
    print(i)