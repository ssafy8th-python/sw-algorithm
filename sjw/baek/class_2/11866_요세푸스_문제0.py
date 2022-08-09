# 11866 요세푸스 문제 0
# 주소: https://www.acmicpc.net/problem/11866

# 제출한 답
# 1 2 3 4 5 6 7
# 4 5 6 7 1 2
# 7 1 2 4 5
# 4 5 7 1
# 1 4 5
# 1 4
# 4

# 4번 인덱스를 기준으로 뒤에를 앞으로 쭉 땡긴뒤 앞에건 뒤로 마지막거 팝
# 반복하다가 길이가 k 보다 작아지면 len % k 한 뒤 앞으로 땡긴뒤 마지막 팝

N, K = map(int, input().split())
num_lst = list(range(1, N + 1))

yose = []

for _ in range(N):
    if len(num_lst) >= K:
        tmp = K
    else:
        tmp = K - len(num_lst)
        while tmp > len(num_lst):
            tmp -= len(num_lst)

    num_lst = num_lst[tmp:] + num_lst[:tmp]
    yose.append(num_lst.pop())

print('<', end='')
for i in yose[0:-1]:
    print(i, end=', ')
print(yose[-1], end='')
print('>')
