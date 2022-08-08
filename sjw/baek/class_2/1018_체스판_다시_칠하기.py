# 1018 체스판 다시 칠하기
# 주소: https://www.acmicpc.net/problem/1018

# 제출한 답
# 1. 8 X 8로 자르기

# 2. 자른 것에서 몇개 색칠해야하는지 세서 해결

# 3. 가장 작은 값 출력

N, M = map(int, input().split())

board = []
count_lst = []
w = 'WBWBWBWB'
b = 'BWBWBWBW'

for _ in range(N):
    board.append(input())

for r_line in range(N-7):
    for c_line in range (M-7):
        temp_board = []
        for i in range(8):
            temp_board.append(board[r_line + i][c_line:c_line + 8])

        count = 0
        for line in range(8):
            if line % 2 == 0:
                if temp_board[line] != w:
                    for B_color, origin_color in zip(temp_board[line], w):
                        if B_color != origin_color:
                            count += 1
            elif line % 2:
                if temp_board[line] != b:
                    for B_color, origin_color in zip(temp_board[line], b):
                        if B_color != origin_color:
                            count += 1
        count_lst.append(count)


        # count = 0
        # for line in range(8):
        #     if line % 2 == 0:
        #         if temp_board[line] != b:
        #             for B_color, origin_color in zip(temp_board[line], b):
        #                 if B_color != origin_color:
        #                     count += 1
        #     elif line % 2:
        #         if temp_board[line] != w:
        #             for B_color, origin_color in zip(temp_board[line], w):
        #                 if B_color != origin_color:
        #                     count += 1
        # count_lst.append(count)

print(min(count_lst))


# 다른 답
row, col = map(int, input().split())          # n, m 받는 것

board = []                                    # wb 받는 곳
ans = 1000                                    # ?

for _ in range(row):                          # wb들을 리스트로 받아서 보드에 넣음(2차원 리스트)
    temp = list(input())
    board.append(temp)

def min (a,b):                                # 최소값 함수? 왜 만들지
    if(a<b): return a
    return b

def solv(endi, endj):                         # 몇 칸 칠해야하는지 세는 함수 / 흰색 보드판인 경우만 계산한 수 64에서 빼서 검은색 보드판도 계산
    cnt = 0
    for i in range(endi-7,endi+1):            # 행
        for j in range(endj-7, endj+1):       # 열
            if (board[i][j]=='W'):            # 선택된 칸이 흰색일 때
                if (i+j)%2:                   # 칸의 좌표를 더한 값이 짝수라면 카운트 +1
                    cnt+=1
            else:                             # 반대로
                if (i+j+1)%2:
                    cnt+=1
    return min(64-cnt, cnt)                   # 헤아린 수와 반대 경우의 수 중 작은 것 리턴

for i in range(7, row):                       # 8 x 8을 옮기는 이중for문
    for j in range(7, col):
        ans = min(ans,solv(i,j))              # 가장 작은 수만 남김

print(ans)