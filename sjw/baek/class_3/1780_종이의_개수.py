# 1780 종이의 개수
# 주소: https://www.acmicpc.net/problem/1780

# 제출한 답
# import sys
# input = sys.stdin.readline

def paper(sr, er, sc, ec, n):
    global m_one, zero, one
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
        if tmp == -1:
            m_one += 1
        elif tmp == 0:
            zero += 1
        else:
            one += 1
        return
    else:
        for r in range(sr, er, n // 3):
            for c in range(sc, ec, n // 3):
                paper(r, r + n // 3, c, c + n // 3, n // 3)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
m_one = 0
zero = 0
one = 0
paper(0, N, 0, N, N)
print(m_one)
print(zero)
print(one)
