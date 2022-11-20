def recursion(s, le, r):
    if le >= r:
        return 1, 1
    elif s[le] != s[r]:
        return 0, 1
    else:
        res, cnt = recursion(s, le+1, r-1)
        return res, cnt + 1


T = int(input())

for _ in range(T):
    s = input()
    print(*recursion(s, 0, len(s) - 1))
