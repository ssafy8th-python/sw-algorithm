A, B, C = map(int, input().split())


if C % 2:
    res = A ^ B
    print(res)
else:
    print(A)
