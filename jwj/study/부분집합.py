
# s라는 상태 값을 같이 넘겨줌
def par(k, s):
    global cnt
    cnt += 1

    if s > 10:
        print('이상', s, result)
        return

    if k == N:
        if s == 10:
            for i in range(N):
                if result[i] == 1:
                    print(lst[i], end=' ')
            print()
    else:
        result[k] = 0
        par(k+1, s)

        result[k] = 1
        par(k+1, s+lst[k])


def per(k):
    if k == N:
        for i in range(N):
            print(lst[result[i]], end=' ')
        print()
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result[k] = i
            per(k+1)
            visited[i] = False


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 10
result = [-1] * N
cnt = 0
par(0, 0)

visited = [False] * N
per(0)

print("cnt : ", cnt)

