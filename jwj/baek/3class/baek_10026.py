from collections import deque
import sys
input = sys.stdin.readline

district = []
num = int(input())
for _ in range(num):
    district.append(list(input()))

visited = []

for _ in range(num):
    visited.append([False] * num)

district_deque = deque()
R = 0
G = 0
RG = 0
B = 0

range_idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for x in range(num):
    for y in range(num):
        if not visited[x][y]:
            visited[x][y] = True
            district_deque.append([x, y])
            if district[x][y] == 'R' or district[x][y] == 'G':
                RG += 1
                while district_deque:
                    position= district_deque.popleft()

                    for i, j in range_idx:
                        x_i = position[0]+i
                        y_j = position[1]+j

                        if (x_i >= 0 and x_i < num) and (y_j >= 0 and y_j < num) and not visited[x_i][y_j] :
                            if district[x_i][y_j] == 'R' or district[x_i][y_j] == 'G':
                                district_deque.append([x_i, y_j])
                                visited[x_i][y_j] = True

            else :
                B+= 1
                while district_deque:
                    position= district_deque.popleft()

                    visited[position[0]][position[1]] = True

                    for i, j in range_idx:
                        x_i = position[0]+i
                        y_j = position[1]+j
                            
                        if (x_i >= 0 and x_i < num) and (y_j >= 0 and y_j < num) and not visited[x_i][y_j] and district[x_i][y_j] == 'B' :

                            district_deque.append([x_i, y_j])
                            visited[x_i][y_j] = True


visited = []

for _ in range(num):
    visited.append([False] * num)

for x in range(num):
    for y in range(num):
        if not visited[x][y]:
            visited[x][y] = True
            
            if district[x][y] == 'R':
                district_deque.append([x, y])
                R += 1
                while district_deque:
                    position= district_deque.popleft()

                    for i, j in range_idx:
                        x_i = position[0]+i
                        y_j = position[1]+j

                        if (x_i >= 0 and x_i < num) and (y_j >= 0 and y_j < num) and not visited[x_i][y_j] :
                            if district[x_i][y_j] == 'R':
                                district_deque.append([x_i, y_j])
                                visited[x_i][y_j] = True

            elif district[x][y] == 'G':
                district_deque.append([x, y])
                G += 1
                while district_deque:
                    position= district_deque.popleft()

                    for i, j in range_idx:
                        x_i = position[0]+i
                        y_j = position[1]+j

                        if (x_i >= 0 and x_i < num) and (y_j >= 0 and y_j < num) and not visited[x_i][y_j] :
                            if district[x_i][y_j] == 'G':
                                district_deque.append([x_i, y_j])
                                visited[x_i][y_j] = True

print(R+G+B, RG + B)

