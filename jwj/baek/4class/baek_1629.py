import sys
input = sys.stdin.readline


def cal(n):
    if n == 1:
        return A % C

    else:
        tmp = cal(n//2)
        if n % 2:
            return (tmp * tmp * A) % C
        else:
            return (tmp * tmp) % C


A, B, C = map(int, input().split())

print(cal(B))
