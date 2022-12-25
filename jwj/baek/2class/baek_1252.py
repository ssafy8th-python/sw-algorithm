A, B = input().split()

if len(A) < len(B):
    A, B = B, A

A = list(map(int, A))
B = list(map(int, B))

check_sum = 0

res = []

for i in range(-1, -len(B) - 1, -1):

    if A[i] + B[i] + check_sum >= 2:
        res.append((A[i] + B[i] + check_sum) % 2)
        check_sum = 1
    else:
        res.append(A[i] + B[i] + check_sum)
        check_sum = 0


for i in range(len(A) - len(B)-1, -1, -1):
    if A[i] + check_sum >= 2:
        res.append((A[i] + check_sum) % 2)
        check_sum = 1
    else:
        res.append(A[i] + check_sum)
        check_sum = 0

res.append(check_sum)

res.reverse()

res = ''.join(str(e) for e in res)

print(int(res))


# a, b = input().split()
#
# result = 0
# int_a = int(a, 2)
# int_b = int(b, 2)
#
# result = int_a + int_b
#
# print(bin(result)[2:])
