import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

lst.sort()

result_lst = [0, 0, 0]

min_value = 5000000000

for i in range(N - 2):
    tmp = lst[i]
    start = i + 1
    end = N - 1

    while start < end:
        n_v = tmp + lst[start] + lst[end]

        if abs(n_v) < min_value:
            min_value = abs(n_v)
            result_lst[0] = i
            result_lst[1] = start
            result_lst[2] = end

        if n_v < 0:
            start += 1
        elif n_v > 0:
            end -= 1
        else:
            break

    if min_value == 0:
        break

for i in result_lst:
    print(lst[i], end=' ')
print()

