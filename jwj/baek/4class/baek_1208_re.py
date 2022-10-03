def subset(last, num):
    lst = [0] * (1 << last)

    for i in range(1 << last):
        for j in range(last):
            if i & (1 << j):
                lst[i] += arr[j + num]

    return lst


N, S = map(int, input().split())
arr = list(map(int, input().split()))

left_num = N//2
right_num = N - left_num

left = subset(left_num, 0)
right = subset(right_num, left_num)

left.sort()
right.sort(reverse=True)

left_idx = 0
right_idx = 0

result = 0

left_num = (1 << left_num)
right_num = (1 << right_num)

while left_idx < left_num and right_idx < right_num:
    new_num = left[left_idx] + right[right_idx]

    if new_num == S:
        right_idx += 1
        left_idx += 1

        # 왼쪽 오른쪽 경우의 수
        c1, c2 = 1, 1

        while left_idx < left_num and left[left_idx] == left[left_idx-1]:
            c1 += 1
            left_idx += 1

        while right_idx < right_num and right[right_idx] == right[right_idx-1]:
            c2 += 1
            right_idx += 1

        result += c1 * c2

        continue

    if new_num > S:
        right_idx += 1
    else:
        left_idx += 1

if S == 0:
    result -= 1

print(result)
