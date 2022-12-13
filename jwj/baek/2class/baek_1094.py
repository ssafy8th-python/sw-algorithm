def cut(bar, target, sum_value):
    if sum_value > target:

        bar1 = bar // 2
        bar2 = bar // 2

        if sum_value - bar1 >= target:
            return cut(bar2, target, sum_value-bar1)
        else:
            return cut(bar2, target, sum_value) + 1
    else:
        return 1


x = int(input())

print(cut(64, x, 64))

