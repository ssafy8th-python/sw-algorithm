son = list(map(int, input().split(":")))
start = list(map(int, input().split(":")))

son_t = son[0] * 3600 + son[1] * 60 + son[2]
start_t = start[0] * 3600 + start[1] * 60 + start[2]

if son_t > start_t:
    start_t = start_t + 24 * 3600

time = abs(son_t - start_t)

hour = time // 3600
time = time % 3600

minute = time // 60
time = time % 60

second = time
print(f'{hour:02}:{minute:02}:{second:02}')
