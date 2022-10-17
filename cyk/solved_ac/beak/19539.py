# 사과나무
# +1, +2 동시에 사용
N = int(input())
tree_height = sorted(list(map(int, input().split())))
a, b = divmod(sum(tree_height), 3)
count = 0
if b == 0:
    for height in tree_height:
        count += height//2
    if count >= a:
        print('YES')
    else:
        print('NO')

else:
    print('NO')
