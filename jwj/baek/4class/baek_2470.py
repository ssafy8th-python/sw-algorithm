N = int(input())

water = list(map(int, input().split()))

water.sort()

result = int(1e12)

start = 0
end = N - 1

result_lst = [0, 0]

while start < end:
    tmp = water[start] + water[end]

    tmp_abs = abs(tmp)

    if tmp_abs < result:
        result = tmp_abs
        result_lst[0] = water[start]
        result_lst[1] = water[end]

    if tmp < 0:
        start += 1
    else:
        end -= 1

print(*result_lst)