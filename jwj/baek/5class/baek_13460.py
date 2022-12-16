import copy


def marble_escape(board, cnt, num):
    global result

    if result <= cnt:
        return

    if cnt == 11:
        return

    # 세로: N, 가로: M
    # 위로 기울이기!!
    if num != 1:
        tmp_board = copy.deepcopy(board)

        for i in range(1, M-1):
            index = 1
            O = 0
            R = 0
            B = 0
            S = []
            isBlue = False

            for j in range(1, N-1):
                char = tmp_board[j][i]
                if char == 'O':
                    O = j
                if char == 'R' or char == 'B':
                    tmp_board[j][i] = '.'
                    tmp_board[index][i] = char
                    index += 1
                    if char == 'R':
                        R = j
                    if char == 'B':
                        B = j
                elif char == '#':
                    S.append(j)
                    index = j + 1

            if O and B and B > O:
                # 중간에 샵이 존재하는지 확인
                for s in S:
                    if O < s < B:
                        break
                else:
                    isBlue = True
                    break

            if O and R and R > O:
                for s in S:
                    if O < s < R:
                        break
                else:
                    if result > cnt:
                        result = cnt
                        return
        if not isBlue:
            marble_escape(tmp_board, cnt + 1, 1)

    if num != 1:
        # 아래로 기울이기!!
        tmp_board = copy.deepcopy(board)

        for i in range(1, M-1):
            index = N - 2
            O = 0
            R = 0
            B = 0
            isBlue = False
            S = []
            for j in range(N-2, 0, -1):
                char = tmp_board[j][i]
                if char == 'O':
                    O = j

                if char == 'R' or char == 'B':
                    tmp_board[j][i] = '.'
                    tmp_board[index][i] = char
                    index -= 1
                    if char == 'R':
                        R = j
                    if char == 'B':
                        B = j

                elif char == '#':
                    S.append(j)
                    index = j - 1

            if O and B and B < O:
                # 중간에 샵이 존재하는지 확인
                for s in S:
                    if B < s < O:
                        break
                else:
                    isBlue = True
                    break

            if O and R and R < O:
                for s in S:
                    if R < s < O:
                        break
                else:
                    if result > cnt:
                        result = cnt
                        return
        if not isBlue:
            marble_escape(tmp_board, cnt + 1, 1)

    if num != 2:
        # 왼쪽으로 기울이기!!
        tmp_board = copy.deepcopy(board)

        for i in range(1, N-1):
            index = 1
            O = 0
            R = 0
            B = 0
            isBlue = False
            S = []
            for j in range(1, M-1):
                char = tmp_board[i][j]
                if char == 'O':
                    O = j
                if char == 'R' or char == 'B':
                    tmp_board[i][j] = '.'
                    tmp_board[i][index] = char
                    index += 1
                    if char == 'R':
                        R = j
                    if char == 'B':
                        B = j
                elif char == '#':
                    S.append(j)
                    index = j + 1

            if O and B and B > O:
                # 중간에 샵이 존재하는지 확인
                for s in S:
                    if O < s < B:
                        break
                else:
                    isBlue = True
                    break

            if O and R and R > O:
                for s in S:
                    if O < s < R:
                        break
                else:
                    if result > cnt:
                        result = cnt
                        return
        if not isBlue:
            marble_escape(tmp_board, cnt + 1, 2)

    if num != 2:
        # 오른쪽으로 기울이기!!
        tmp_board = copy.deepcopy(board)

        for i in range(1, N-1):
            index = M - 2
            O = 0
            R = 0
            B = 0
            S = []
            isBlue = False
            for j in range(M-2, 0, -1):
                char = tmp_board[i][j]
                if char == 'O':
                    O = j
                if char == 'R' or char == 'B':
                    tmp_board[i][j] = '.'
                    tmp_board[i][index] = char
                    index -= 1
                    if char == 'R':
                        R = j
                    if char == 'B':
                        B = j
                elif char == '#':
                    S.append(j)
                    index = j - 1

            if O and B and B < O:
                # 중간에 샵이 존재하는지 확인
                for s in S:
                    if B < s < O:
                        break
                else:
                    isBlue = True
                    break

            if O and R and R < O:
                for s in S:
                    if R < s < O:
                        break
                else:
                    if result > cnt:
                        result = cnt
                        return
        if not isBlue:
            marble_escape(tmp_board, cnt + 1, 2)


result = 100

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

marble_escape(board, 1, 0)

if result == 100:
    print(-1)
else:
    print(result)