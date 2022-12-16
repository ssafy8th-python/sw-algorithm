T = int(input())

for _ in range(T):
    h, w = map(int, input().split())

    building = [list(input()) for _ in range(h)]

    key = list(input())

    enters = []

    gates = []

    visited = [[False] * w for _ in range(h)]
    result = 0
    # 앞, 뒤
    for col in (0, h-1):
        for i in range(w):
            visited[col][i] = True
            char = building[col][i]
            if char == '*':
                continue
            elif char == '.':
                enters.append((col, i))
            elif chr(ord(char) + 32) in key:
                enters.append((col, i))
            elif 97 <= ord(char) <= 122:
                enters.append((col, i))
                key.append(char)
                tmp_char = chr(ord(char) - 32)
                for gate, index in enumerate(gates):
                    if tmp_char == gate[0]:
                        enters.append((gate[1], gate[2]))
                        gates.pop(index)
            elif char == '$':
                enters.append((col, i))
                result += 1
            else:
                gates.append((char, col, i))
    # 양 옆
    for row in (0, w-1):
        for i in range(1, h - 1):
            visited[i][row] = True
            char = building[i][row]
            if char == '*':
                continue
            elif char == '.':
                enters.append((i, row))
            elif chr(ord(char) + 32) in key:
                enters.append((i, row))
            elif 97 <= ord(char) <= 122:
                enters.append((i, row))
                key.append(char)
                tmp_char = chr(ord(char) - 32)
                for gate, index in enumerate(gates):
                    if tmp_char == gate[0]:
                        enters.append((gate[1], gate[2]))
                        gates.pop(index)
            elif char == '$':
                enters.append((i, row))
                result += 1
            else:
                gates.append((char, i, row))

    while enters:
        x, y = enters.pop()

        for d_x, d_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n_x, n_y = x + d_x, y + d_y
            if 0 <= n_x < h and 0 <= n_y < w and not visited[n_x][n_y]:
                visited[n_x][n_y] = True
                char = building[n_x][n_y]
                if char == '*':
                    continue
                elif char == '.':
                    enters.append((n_x, n_y))
                elif char == '$':
                    enters.append((n_x, n_y))
                    result += 1
                elif 97 <= ord(char) <= 122:
                    enters.append((n_x, n_y))
                    key.append(char)
                    tmp_char = chr(ord(char) - 32)
                    for index, gate in enumerate(gates):
                        if tmp_char == gate[0]:
                            enters.append((gate[1], gate[2]))
                            gates.pop(index)
                elif chr(ord(char) + 32) in key:
                    enters.append((n_x, n_y))
                else:
                    gates.append((char, n_x, n_y))
    print(result)
