# 개미
'''
6 4     총 좌표
4 1     초기 위치 좌표
8       개미가 움직인 시간
'''

boundary_col, boundary_row = map(int, input().split())
st_col, st_row = map(int, input().split())
time = int(input())

res_col = (time + st_col) % boundary_col
q_col = (time + st_col) // boundary_col
res_row = (time + st_row) % boundary_row
q_row = (time + st_row) // boundary_row

result_col, result_row = 0, 0


if q_col % 2:
    result_col = boundary_col - res_col
else:
    result_col = res_col
if q_row % 2:
    result_row = boundary_row - res_row
else:
    result_row = res_row

print(result_col, result_row)